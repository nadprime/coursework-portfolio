# System Design

<div align="center">
  <strong>🏗️ Building Scalable Systems 🏗️</strong><br>
  <em>From fundamentals to distributed architecture</em>
</div>

---

## 📖 Overview

This section covers system design principles, patterns, and case studies for building scalable, reliable, and maintainable systems. Essential for technical interviews and real-world software architecture.

## 🎯 Learning Objectives

- Understand how to design systems that scale
- Master trade-offs in distributed systems
- Learn common architectural patterns
- Prepare for system design interviews
- Build intuition for real-world system constraints

---

## 🗂️ Directory Structure

```
System-Design/
├── Fundamentals/
│   ├── scalability.md
│   ├── availability.md
│   ├── reliability.md
│   ├── performance.md
│   ├── consistency.md
│   └── trade-offs.md
├── Components/
│   ├── load-balancers.md
│   ├── caching.md
│   ├── databases.md
│   ├── message-queues.md
│   ├── cdn.md
│   └── api-gateways.md
├── Patterns/
│   ├── microservices.md
│   ├── event-driven.md
│   ├── cqrs.md
│   ├── saga.md
│   └── circuit-breaker.md
├── Case-Studies/
│   ├── url-shortener.md
│   ├── pastebin.md
│   ├── instagram.md
│   ├── twitter.md
│   ├── youtube.md
│   ├── uber.md
│   └── whatsapp.md
├── Concepts/
│   ├── cap-theorem.md
│   ├── acid-base.md
│   ├── sharding.md
│   ├── replication.md
│   └── partitioning.md
└── README.md
```

---

## 📚 Core Concepts

### 1️⃣ Scalability

#### Vertical Scaling (Scale Up)
- **Definition:** Adding more power to existing machines
- **Pros:** Simple, no code changes
- **Cons:** Hardware limits, single point of failure, expensive
- **When to use:** Early stages, specific workload requirements

#### Horizontal Scaling (Scale Out)
- **Definition:** Adding more machines
- **Pros:** No limits, redundancy, cost-effective
- **Cons:** Complex, data consistency challenges
- **When to use:** High growth, distributed systems

#### Scaling Strategies
- **Load Balancing** - Distribute traffic across servers
- **Caching** - Reduce database load
- **Database Sharding** - Partition data across databases
- **Asynchronous Processing** - Offload heavy tasks
- **Microservices** - Independent scaling per service

---

### 2️⃣ Availability

#### High Availability Patterns
- **Redundancy** - Eliminate single points of failure
- **Failover** - Automatic switch to backup system
- **Replication** - Duplicate data across locations
- **Health Checks** - Monitor and detect failures
- **Load Balancing** - Route traffic away from failed nodes

#### Availability Metrics
```
Availability = (Uptime / Total Time) × 100%

99% (Two nines)     = 3.65 days downtime/year
99.9% (Three nines) = 8.76 hours downtime/year
99.99% (Four nines) = 52.56 minutes downtime/year
99.999% (Five nines) = 5.26 minutes downtime/year
```

---

### 3️⃣ Consistency

#### Consistency Models
| Model | Description | Use Case |
|:------|:------------|:---------|
| **Strong Consistency** | All nodes see same data simultaneously | Banking, financial transactions |
| **Eventual Consistency** | Nodes eventually converge to same state | Social media feeds, comments |
| **Weak Consistency** | No guarantee when data becomes consistent | Live streaming, gaming |

#### CAP Theorem
**You can only guarantee 2 of 3:**
- **C**onsistency - All nodes see the same data
- **A**vailability - Every request gets a response
- **P**artition Tolerance - System works despite network failures

**Trade-offs:**
- **CP Systems:** Consistent + Partition Tolerant (MongoDB, HBase)
- **AP Systems:** Available + Partition Tolerant (Cassandra, DynamoDB)
- **CA Systems:** Consistent + Available (Traditional RDBMS - theoretical)

---

### 4️⃣ Databases

#### SQL vs NoSQL

**SQL (Relational)**
- **Structure:** Predefined schema, tables with relationships
- **ACID:** Atomicity, Consistency, Isolation, Durability
- **Examples:** PostgreSQL, MySQL, Oracle
- **Use Cases:** 
  - Complex queries and joins
  - Transactions critical (banking)
  - Structured data with relationships
  - Strong consistency requirements

**NoSQL (Non-Relational)**
- **Structure:** Flexible schema, various data models
- **BASE:** Basically Available, Soft state, Eventual consistency
- **Types:**
  - **Document:** MongoDB, CouchDB
  - **Key-Value:** Redis, DynamoDB
  - **Column-Family:** Cassandra, HBase
  - **Graph:** Neo4j, Amazon Neptune
- **Use Cases:**
  - Massive scale and high throughput
  - Flexible/evolving schema
  - High availability over consistency
  - Unstructured or semi-structured data

#### Database Scaling Techniques

**Replication**
- **Master-Slave:** Master handles writes, slaves handle reads
- **Master-Master:** Multiple masters handle writes
- **Benefits:** Read scaling, redundancy
- **Challenges:** Replication lag, consistency

**Sharding (Partitioning)**
- **Horizontal:** Split rows across databases
- **Vertical:** Split columns into different tables
- **Strategies:**
  - Range-based (user_id 1-1000, 1001-2000)
  - Hash-based (hash(user_id) % num_shards)
  - Geographic (by region)
- **Challenges:** Rebalancing, distributed queries, cross-shard joins

**Indexing**
- B-tree indexes for range queries
- Hash indexes for exact matches
- Composite indexes for multiple columns
- Full-text indexes for search

---

### 5️⃣ Caching

#### Cache Levels
```
Client Browser → CDN → Application Cache → Database Cache → Database
```

#### Caching Strategies

**Cache-Aside (Lazy Loading)**
```
1. Check cache
2. If miss, query database
3. Store in cache
4. Return data
```
- **Pros:** Load only what's needed
- **Cons:** Cache miss penalty

**Write-Through**
```
1. Write to cache AND database
2. Return success
```
- **Pros:** Cache always up-to-date
- **Cons:** Slower writes

**Write-Back (Write-Behind)**
```
1. Write to cache
2. Async write to database
```
- **Pros:** Fast writes
- **Cons:** Risk of data loss

**Refresh-Ahead**
```
Automatically refresh cache before expiration
```
- **Pros:** Low latency
- **Cons:** Wasted resources if not accessed

#### Cache Eviction Policies
- **LRU** (Least Recently Used) - Remove oldest accessed
- **LFU** (Least Frequently Used) - Remove least accessed
- **FIFO** (First In First Out) - Remove oldest entry
- **TTL** (Time To Live) - Remove after time expired

#### Popular Cache Technologies
- **Redis** - In-memory data store, key-value
- **Memcached** - Distributed memory caching
- **CDN** - Cloudflare, AWS CloudFront, Akamai
- **Application-level** - Built-in caching (Django cache)

---

### 6️⃣ Load Balancing

#### Load Balancer Algorithms
| Algorithm | Description | Use Case |
|:----------|:------------|:---------|
| **Round Robin** | Distribute requests sequentially | Servers with equal capacity |
| **Least Connections** | Route to server with fewest connections | Long-lived connections |
| **Least Response Time** | Route to fastest responding server | Varying server performance |
| **IP Hash** | Hash client IP to same server | Session persistence |
| **Weighted Round Robin** | Distribute based on server capacity | Heterogeneous servers |

#### Load Balancer Types
- **Hardware:** F5, Citrix NetScaler (expensive, high performance)
- **Software:** Nginx, HAProxy, Envoy (flexible, cost-effective)
- **Cloud:** AWS ALB/NLB, Google Cloud Load Balancer

#### Layer 4 vs Layer 7 Load Balancing
- **Layer 4 (Transport):** Routes based on IP/Port, faster, less flexible
- **Layer 7 (Application):** Routes based on content (URL, headers), slower, more flexible

---

### 7️⃣ Message Queues

#### Purpose
- Asynchronous communication
- Decouple services
- Handle traffic spikes
- Retry failed operations
- Order processing

#### Queue Patterns

**Point-to-Point**
```
Producer → Queue → Consumer
```
- One message to one consumer

**Publish-Subscribe**
```
Publisher → Topic → Multiple Subscribers
```
- One message to many consumers

#### Popular Message Queues
- **RabbitMQ** - Traditional message broker, AMQP protocol
- **Apache Kafka** - Distributed streaming platform, high throughput
- **AWS SQS** - Managed queue service
- **Redis Pub/Sub** - Lightweight messaging
- **Apache Pulsar** - Multi-tenancy, geo-replication

---

### 8️⃣ API Design

#### RESTful API Principles
- **Resources:** Nouns (users, posts, comments)
- **HTTP Methods:** GET, POST, PUT, DELETE, PATCH
- **Stateless:** Each request independent
- **URI Structure:** `/api/v1/users/{id}/posts`

#### Status Codes
```
2xx - Success
  200 OK - Request succeeded
  201 Created - Resource created
  204 No Content - Success, no body

4xx - Client Error
  400 Bad Request - Invalid input
  401 Unauthorized - Authentication required
  403 Forbidden - Authenticated but not allowed
  404 Not Found - Resource doesn't exist

5xx - Server Error
  500 Internal Server Error - Generic error
  503 Service Unavailable - Temporary unavailable
```

#### API Rate Limiting
- **Token Bucket** - Tokens added at fixed rate
- **Leaky Bucket** - Requests processed at fixed rate
- **Fixed Window** - X requests per time window
- **Sliding Window** - More accurate than fixed window

#### API Versioning
- **URI:** `/api/v1/users`, `/api/v2/users`
- **Header:** `Accept: application/vnd.company.v1+json`
- **Query Parameter:** `/api/users?version=1`

---

## 🏗️ Common System Design Patterns

### Microservices Architecture
**Characteristics:**
- Independently deployable services
- Each service owns its data
- Communication via APIs (REST/gRPC)
- Technology heterogeneity

**Pros:**
- Scalability per service
- Independent deployment
- Technology flexibility
- Fault isolation

**Cons:**
- Distributed system complexity
- Network latency
- Data consistency challenges
- Increased operational overhead

### Event-Driven Architecture
**Components:**
- Event producers
- Event bus/broker
- Event consumers

**Benefits:**
- Loose coupling
- Scalability
- Real-time processing
- Resilience

### CQRS (Command Query Responsibility Segregation)
**Concept:** Separate read and write operations

**Write Model:** Handle commands (updates)  
**Read Model:** Handle queries (reads)

**Use Cases:**
- Different read/write patterns
- Complex domain logic
- Event sourcing

---

## 📊 System Design Interview Framework

### Step-by-Step Approach

#### 1. Requirements (5 minutes)
**Functional Requirements:**
- What features must the system support?
- Core use cases?

**Non-Functional Requirements:**
- Scale: Users? Requests per second?
- Performance: Latency requirements?
- Availability: Uptime requirements?
- Consistency: Strong or eventual?

**Out of Scope:**
- What are we NOT building?

#### 2. Estimations (5 minutes)
**Calculate:**
- Daily Active Users (DAU)
- Requests per second: `DAU × actions/day / 86400`
- Storage: `data_per_item × items_per_day × retention_days`
- Bandwidth: `request_size × requests/second`

**Example:**
```
100M DAU
Each user posts 2 times/day
Post size: 1KB
   
Writes: 100M × 2 / 86400 = ~2,300 writes/sec
Storage: 1KB × 200M posts/day × 365 days = ~73TB/year
```

#### 3. High-Level Design (15 minutes)
- Draw main components (boxes and arrows)
- Show data flow
- Define APIs
- Database schema

#### 4. Deep Dive (20 minutes)
**Address:**
- Bottlenecks
- Single points of failure
- Scaling strategy
- Data partitioning
- Caching strategy
- Trade-offs

#### 5. Wrap Up (5 minutes)
- Monitoring and metrics
- Security considerations
- Future enhancements

---

## 📝 Case Studies

### Design URL Shortener (e.g., bit.ly)

**Requirements:**
- Shorten long URLs
- Redirect to original URL
- Custom aliases (optional)
- Analytics (optional)

**Key Points:**
- **Encoding:** Base62 (a-z, A-Z, 0-9) for short codes
- **Database:** Key-value store (URL → Short code)
- **Caching:** Cache popular URLs
- **Scale:** Billions of URLs

**Design:**
```
[User] → [Load Balancer] → [App Servers] → [Cache] → [Database]
                                          ↓
                                    [Analytics Service]
```

### Design Twitter

**Requirements:**
- Post tweets
- Follow users
- Timeline (home + user)
- Trending topics

**Key Points:**
- **Feed Generation:** Fan-out on write vs read
- **Storage:** User data (SQL), tweets (NoSQL)
- **Caching:** Timeline cache
- **Scale:** 300M users, 500M tweets/day

### Design Instagram

**Requirements:**
- Upload photos
- Follow users
- Feed with photos
- Like and comment

**Key Points:**
- **Storage:** Photo storage (S3), metadata (DB)
- **CDN:** Serve images globally
- **Feed Ranking:** Algorithm to show relevant posts
- **Scale:** Photo storage, high traffic

---

## 📚 Resources

### Books
- ⭐ **"Designing Data-Intensive Applications"** by Martin Kleppmann
- ⭐ **"System Design Interview Vol 1 & 2"** by Alex Xu
- "Building Microservices" by Sam Newman
- "Database Internals" by Alex Petrov

### Online Courses
- [Grokking the System Design Interview](https://www.educative.io/)
- [System Design Primer (GitHub)](https://github.com/donnemartin/system-design-primer)
- [ByteByteGo Newsletter](https://blog.bytebytego.com/)

### YouTube Channels
- **Gaurav Sen** - System design concepts
- **Tech Dummies** - Case studies
- **sudoCODE** - Interview prep
- **System Design Interview** - Real examples

### Websites & Blogs
- High Scalability blog
- AWS Architecture Blog
- Engineering blogs: Netflix, Uber, Airbnb
- Papers We Love (distributed systems papers)

---

## 🎯 Learning Path

### Phase 1: Fundamentals (Weeks 1-2)
- [ ] Scalability concepts
- [ ] Load balancing
- [ ] Caching strategies
- [ ] Database basics

### Phase 2: Components (Weeks 3-4)
- [ ] Different database types
- [ ] Message queues
- [ ] CDN
- [ ] Microservices intro

### Phase 3: Advanced (Weeks 5-6)
- [ ] CAP theorem
- [ ] Consistency patterns
- [ ] Sharding strategies
- [ ] Distributed systems

### Phase 4: Practice (Weeks 7-8)
- [ ] 10+ case studies
- [ ] Mock interviews
- [ ] Draw diagrams
- [ ] Explain trade-offs

---

## 📈 Progress Tracking

### Concepts Mastered: 0/20
- [ ] Scalability (horizontal/vertical)
- [ ] Load balancing
- [ ] Caching
- [ ] SQL vs NoSQL
- [ ] Database replication
- [ ] Database sharding
- [ ] CAP theorem
- [ ] Consistency models
- [ ] Message queues
- [ ] CDN

### Case Studies Completed: 0/15
- [ ] URL Shortener
- [ ] Pastebin
- [ ] Instagram
- [ ] Twitter
- [ ] YouTube
- [ ] Uber
- [ ] WhatsApp

### Mock Designs: 0/10

---

## 💡 Tips for Success

### During Interview
- ✅ Ask clarifying questions
- ✅ Think out loud
- ✅ Start with high-level design
- ✅ Justify decisions
- ✅ Discuss trade-offs
- ✅ Be honest about unknowns

### Communication
- ✅ Use diagrams (boxes and arrows)
- ✅ Define terminology
- ✅ Explain alternatives considered
- ✅ Discuss failure scenarios
- ✅ Talk about monitoring

### Common Mistakes
- ❌ Jumping to implementation
- ❌ Not asking questions
- ❌ Over-engineering
- ❌ Ignoring constraints
- ❌ Not considering trade-offs

---

<div align="center">
  <em>"Good architecture is not about the solution, it's about handling trade-offs"</em><br>
  <strong>Think scale, design resilience, embrace trade-offs</strong><br><br>
  <small>Last Updated: February 2026</small>
</div>
