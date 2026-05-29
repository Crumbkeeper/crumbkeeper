from fastapi import Query


def search_filter(
    search: str | None = Query(
        None
    ),
):
    return search


def active_filter(
    active: bool | None = Query(
        None
    ),
):
    return active
