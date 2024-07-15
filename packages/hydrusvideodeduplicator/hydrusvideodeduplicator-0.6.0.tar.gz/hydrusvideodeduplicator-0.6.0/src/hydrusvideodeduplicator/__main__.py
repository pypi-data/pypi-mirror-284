from __future__ import annotations

import logging
from typing import Annotated, List, Optional

import typer
from rich import print

import hydrusvideodeduplicator.hydrus_api as hydrus_api

from .__about__ import __version__
from .client import HVDClient
from .config import (
    HYDRUS_API_KEY,
    HYDRUS_API_URL,
    HYDRUS_LOCAL_FILE_SERVICE_KEYS,
    HYDRUS_QUERY,
    REQUESTS_CA_BUNDLE,
    FAILED_PAGE_NAME,
)
from .db import DedupeDB
from .dedup import HydrusVideoDeduplicator

"""
Parameters:
- api_key will be read from env var $HYDRUS_API_KEY or .env file
- api_url will be read from env var $HYDRUS_API_URL or .env file
- to add custom queries, do
  --custom-query="series:twilight" --custom-query="character:edward" ... etc for each query
- threshold is the min % matching to be considered similar. 100% is identical.
- verbose turns on logging
- debug turns on logging and sets the logging level to debug
"""
print(f"[blue] Hydrus Video Deduplicator {__version__} [/]")


def main(
    api_key: Annotated[Optional[str], typer.Option(help="Hydrus API Key")] = None,
    api_url: Annotated[Optional[str], typer.Option(help="Hydrus API URL")] = HYDRUS_API_URL,
    overwrite: Annotated[Optional[bool], typer.Option(help="Overwrite existing perceptual hashes")] = False,
    query: Annotated[Optional[List[str]], typer.Option(help="Custom Hydrus tag query")] = HYDRUS_QUERY,
    threshold: Annotated[
        Optional[float], typer.Option(help="Similarity threshold for a pair of videos where 100 is identical")
    ] = 75.0,
    skip_hashing: Annotated[
        Optional[bool], typer.Option(help="Skip perceptual hashing and just search for duplicates")
    ] = False,
    file_service_key: Annotated[
        Optional[List[str]], typer.Option(help="Local file service key")
    ] = HYDRUS_LOCAL_FILE_SERVICE_KEYS,
    verify_cert: Annotated[
        Optional[str], typer.Option(help="Path to TLS cert. This forces verification.")
    ] = REQUESTS_CA_BUNDLE,
    clear_search_cache: Annotated[
        Optional[bool], typer.Option(help="Clear the cache that tracks what files have already been compared")
    ] = False,
    failed_page_name: Annotated[
        Optional[str], typer.Option(help="The name of the Hydrus page to add failed files to.")
    ] = FAILED_PAGE_NAME,
    job_count: Annotated[
        Optional[int], typer.Option(help="Number of CPU threads to use. Default is all but one core.")
    ] = -2,
    verbose: Annotated[Optional[bool], typer.Option(help="Verbose logging")] = False,
    debug: Annotated[Optional[bool], typer.Option(hidden=True)] = False,
):
    # Fix mypy errors from optional parameters
    assert overwrite is not None and threshold is not None and skip_hashing is not None and job_count is not None

    # CLI debug parameter sets log level to info or debug
    loglevel = logging.INFO
    if debug:
        loglevel = logging.DEBUG
        verbose = True

    logging.basicConfig(format=' %(asctime)s - %(name)s: %(message)s', datefmt='%H:%M:%S', level=loglevel)

    # Verbose sets whether logs are shown to the user at all.
    # Logs are separate from printing in this program.
    if not verbose:
        logging.disable()

    logging.info("Starting Hydrus Video Deduplicator")

    # Clear cache
    if clear_search_cache:
        DedupeDB.clear_search_cache()

    # CLI overwrites env vars with no default value
    if not api_key:
        api_key = HYDRUS_API_KEY

    # Check for necessary variables
    if not api_key:
        print("API key not set. Exiting...")
        raise typer.Exit(code=1)
    # This should not happen because there's a default val in secret.py
    if not api_url:
        print("Hydrus URL not set. Exiting...")
        raise typer.Exit(code=1)

    # Client connection
    # TODO: Try to connect with https first and then fallback to http with a strong warning
    print(f"Connecting to {api_url}")
    error_connecting = True
    error_connecting_exception_msg = ""
    error_connecting_exception = ""
    try:
        hvdclient = HVDClient(
            file_service_keys=file_service_key,
            api_url=api_url,
            access_key=api_key,
            verify_cert=verify_cert,
        )
    except hydrus_api.InsufficientAccess as exc:
        error_connecting_exception_msg = "Invalid Hydrus API key."
        error_connecting_exception = str(exc)
    except hydrus_api.DatabaseLocked as exc:
        error_connecting_exception_msg = "Hydrus database is locked. Try again later."
        error_connecting_exception = str(exc)
    except hydrus_api.ServerError as exc:
        error_connecting_exception_msg = "Unknown Server Error."
        error_connecting_exception = str(exc)
    except hydrus_api.APIError as exc:
        error_connecting_exception_msg = "API Error"
        error_connecting_exception = str(exc)
    except hydrus_api.ConnectionError as exc:
        # Probably SSL error
        if "SSL" in str(exc):
            error_connecting_exception_msg = "Failed to connect to Hydrus. SSL certificate verification failed."
        # Probably tried using http instead of https when client is https
        elif "Connection aborted" in str(exc):
            error_connecting_exception_msg = (
                "Failed to connect to Hydrus. Does your Hydrus Client API http/https setting match your --api-url?"
            )
        else:
            error_connecting_exception_msg = "Failed to connect to Hydrus. Is your Hydrus instance running?"
        error_connecting_exception = str(exc)
    else:
        error_connecting = False

    if error_connecting:
        logging.fatal("FATAL ERROR HAS OCCURRED")
        logging.fatal(str(error_connecting_exception))
        print(f"[red] {str(error_connecting_exception_msg)} ")
        raise typer.Exit(code=1)

    if debug:
        HVDClient._log.setLevel(logging.DEBUG)

    # Deduplication

    deduper = HydrusVideoDeduplicator(client=hvdclient, job_count=job_count, failed_page_name=failed_page_name)

    if debug:
        deduper.hydlog.setLevel(logging.DEBUG)
        deduper._DEBUG = True

    if threshold < 0.0 or threshold > 100.0:
        print("[red] ERROR: Invalid similarity threshold. Must be between 0 and 100.")
        raise typer.Exit(code=1)
    HydrusVideoDeduplicator.threshold = threshold

    DedupeDB.clear_trashed_files_from_db(hvdclient)

    deduper.deduplicate(
        overwrite=overwrite,
        custom_query=query,
        skip_hashing=skip_hashing,
    )

    raise typer.Exit()


try:
    typer.run(main)
except KeyboardInterrupt as exc:
    raise typer.Exit(-1) from exc
