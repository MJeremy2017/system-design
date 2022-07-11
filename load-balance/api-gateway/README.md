# API Gateway

API gateway sits in front of a set of **different microservices** and can direct traffic to different service based
on the configured rules.

It also supports rate limiting, SSL termination, authentication, IP whitelisting, servicing static content, etc.

## API Gateway vs. Load Balancer

- LB normally direct traffic evenly to the same set of services while API Gateway can be configured to direct requests to specific resources based on the endpoints being requested.
- API Gateway offers many additional features missing in LB. For example, it handles authentication and authorization, API token issuance and management, and can even generate SDKs based on the API structure.

