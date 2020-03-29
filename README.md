# httplogger
A small [mitmproxy](https://github.com/mitmproxy/mitmproxy) addon to log complete request and response bodies, headers etc into a database table

The table with required structure can be created using following statement.
```
CREATE TABLE log (
    request_body text,
    response_body text,
    request_headers text,
    response_headers text,
    time datetime default CURRENT_TIMESTAMP,
    rtt real,
    method text,
    url text,
    code integer
);
```
