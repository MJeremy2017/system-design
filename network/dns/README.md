# DNS (Domain Name Service)

![img.png](dns.png)

`DNS` maps a domain name to a specific IP address. For example, maps `www.example.com` to `172.01.11.03`.
`DNS` is hierarchical, with a few authoritative servers at the top level. Your router or ISP provides 
information about which `DNS` server(s) to contact when doing a lookup.

- `DNS` results can be cached by your browser for some time based on TTL.
- Some cloud service providers like AWS `Route53` all manages `DNS` service.

**Key Words**

- `A record` (address) - Points a name to an IP address.
- `CNAME` (canonical) - Points a name to another name or CNAME (example.com to www.example.com) or to an A record.
