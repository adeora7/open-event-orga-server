from sqlalchemy import or_, func

from open_event.models.event import Event


def extract_special_queries(queries):
    """
    Separate special queries from normal queries
    """
    specials = {}
    dc = queries.copy()
    for i in queries:
        if i.startswith('__') and i in FILTERS_LIST:
            specials[i] = queries[i]
            del dc[i]
    return (dc, specials)


def apply_special_queries(query, specials):
    """
    Apply all special queries on the current
    existing :query (set)
    """
    for i in specials:
        query = FILTERS_LIST[i](specials[i], query)
    return query


#######
# DEFINE CUSTOM FILTERS BELOW
#######


def event_contains(value, query):
    value = value.lower()
    q = query.filter(or_(
        func.lower(Event.name).contains(value),
        func.lower(Event.description).contains(value)
    ))
    return q


#######
# ADD CUSTOM FILTERS TO LIST
#######


FILTERS_LIST = {
    '__event_contains': event_contains
}
