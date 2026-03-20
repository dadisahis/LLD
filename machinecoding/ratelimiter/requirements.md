

Functional Requirements:
1. Support Rate limit on per user basis
2. Enfore a fixed no of allowed requests within a defined time
3. Reject request that exceed allowed limit and return appropriate response
4. Provide a simple way to simulate requests in a demo or main method

NFR: 
thread safe
modular
extensible
performace 

Core Entities
1. RateLimitStrategy - Interface - define allowed request
2. Fixed Window Strategy - Concrete Class 
3. Token Bucket Strategy -  Concrete Class
4. Rate Limit Service - Concrete Class -  Singleton and Facae 