# Database Fundamental Notes

## Week 2 Design Process

### Conceptual Design
Used to design the database model without any physical aspect.
- ER Diagram:
    - **Entity**: an object (type of thing)
    - **Connection**: relationship between different entities
    - **Attribute**: it describes the property of an entity

#### Attributes
Properties of entities in the model
- Candidate Key **{CK}**: An attribute or a set of attribute that can be used to uniquely identify a speicific instance of an entity
- Primary Key **{PK}**: a minimal super key selected from candidate key which can identify instances of an entity. **{PPK}** when multiple attribute form the primary key, also called **Composite Key**.
- Composite Attribute: attribute made up with multiple pieces of data 
(e.g. address)
- Multi-value Attribute: attributes that can contain a list of data of the 
same type (e.g. list of phone numbers)
- Derived Attribute: attributes that can derived or calculated from 
other attributes.

#### Fan Trap
Layout obscures relationship betwwen entity A and entity B. 
Assume there are entity A, B and C.
Resturcute such that A - C - B (A connects to C and C connects to B)

#### Chasm Trap
Assume there are entity A, B and C. Since B relationship between B and C 
is optional (B -> C * and C -> B 0..1), C might connect to nothing. 
Hence, adding a direct connection between A and C solves the issue.

#### Enhanced ER modeling (EER)
ER with ability to visualise OOP concepts including inheritance and superclasses.

#### Inheritance Relationship
- Participation Constraint: whether a member of a superclass is required to 
be a member of at least one subclass or not. (**Mandatory** vs **Optional**)
- Disjoing Constraint: whether an entity instance is allow to belong to 
multiple subclass or not. (**And** vs **Or**)

- Four Types:
    - Mandatory and disjoint (must belong to exactly one subclass).
    - Optional and disjoint (can belong to up to one subclass).
    - Mandatory and nondisjoint (must belong to at least one subclass).
    - Optional and nondisjoint (can belong to any number of subclasses).

### Logical Design
Defining structure of data in more detail with a particular data model 
(relational, object-oriented, graph-based, etc). 
Design the schema needed to implement the database

- Translate from ER diagram (top-down method)
- Start with one big data table and normalise (bottom-up method)

#### ER Diagram Translation
Identify strong and week entities.

- Relationship
    - 1:*
    - 1:1
    - 1:1 recursive
    - \*:\*

![abc](../docs/assets/er_translation.png)

Result will be in third normal form. 

### Normalisation

Goal of normalisation is to minimise unnecessary duplicated data, 
which can cause update anomalies. Normalisation also helps avoid
- inconsistent data
- unintended loss

#### Level of Normalisation
- Unnormalised Form (UNF)
- First (1NF) 
- second (2NF) 
- third (3NF) 
- Boyce-Codd normal form (BCNF) 

#### Normalisation Process

##### UNF
No special properties

##### 1NF
No repeating groups (no multi-valued attribute or set of attributes)

##### UNF -> 1NF
- Flattening: separating data into multiple rows
- Breaking: breaking down multi-valued data into its own table using 
the original table's primary key as new table's primary, and give each piece 
of data its own row. 

##### 2NF
2NF means there are no non-primary-key attributes that are fully
determined by a part of the primary key. 
(No partial dependencies on the primary key in a table.) 

A **functinally determines** B (A ® B) if having A to be a specific value 
causes B to be determined. For example, having staffNo can 
determine position but having position cannot determine staffNo. 

**Full functional dependency**: B is determined by the full set of A’s
values. 

**Partial functional dependency**: Only part of A is needed to
determine the value of B. 

##### 1NF -> 2NF
Whenever you find an attribute(s) that is dependent on
(functionally determined by) only part of the primary key, create a
new table with (1) a copy of the primary key part, and (2) the
attributes it fully determines.

##### 3NF
Third normal form (3NF) ensures that there are no non-primarykey
attributes transitively dependent on the primary key. 
(Every non-primary-key attribute should depend on the whole key)

A transitive dependency is when you have A ® B and B ® C 
(meaning that A ® C). 

##### 2NF -> 3NF
For primary key A, if you have A ® B and B ® C, split B and C into 
their own table (primary key: B).
▪ Keep B (but not C) in the original table along with A. B functions as 
a foreign key to the new table.

##### BCNF
BCNF requires every functional dependency determinant (left side) 
to be a candidate key for the table. (Every attribute should depend on the whole key)

##### 3NF -> BCNF
Spin that problematic functional dependency into its own table. 
Retain the determinant (left side) as a foreign key in the original table.

Example: 
- 3NF: Teaching (pupil, subject, teacher)
- BCNF: Tutor (pupil, teacher) and TaughtSubject (teacher, subject)

## Week 3 Database Storage and Relatinal Algebra

### Units of Storage
- Block: fixed-length unit of storage; 
smallest unit of data that can be read or allocated. 
Usually ~4-8 kb.
- Page: fixed-length unit of data used in memory management

#### Fixed-length Records
Fixed-length records/fields can simplify storage/storage operations
- Number of records per block is known in advance. 
- New records can fill the place of deleted records 
if order is not important. 
- bKeep track of empty slots with a "free list". 

#### Variable-length Records
- Records with variable-length fields can be implemented by 
storing two pieces of metadata per record: 
**offset** (location) and **length** (size).
- Variable-length records can be stored within a block (or page) 
with a **slotted-page** structure.
    - Block storage is "eaten" at two different ends and meets in the middle.
    - Top: header with offset/length metadata on all records in that block.
    - Bottom: the records stored contiguously.

#### Buffers
Temporary memory storage for data that is being (1) processed or 
(2) transferred elsewhere.

In database context, a buffer is anywhere storing (temporary) 
copies of data outside of the database (for reading or updating purposes). 

- If space is limited, some data (pages) not being (recently) used may be overwritten.
    - If this space contains updated database data, the updated data should be written to the database (dirty page).

- "**Flushing buffers**" means writing all data contained in buffers 
to long-term storage.
    - Clear out all data so that all of temporary storage is available to be used again.

#### Indexes
a data structure to aid in the quick data retrieval (random access) 
of specific records in a table

Types of indexes:
- Clustering/clustered vs. nonclustered (or primary vs. secondary indexes).
- For clustered indexes: Dense vs. sparse.
- Single-level vs. multilevel.

Clustered (primary index): 
the attribute or set of attributes that determine the order that 
records in a relation are physically stored. (sorted attributes)

Note that records are physically stored by primary index.

Nonclustered (secondary index):
an additional index defined on a table that differ from the way that 
the table is stored intrinsically. (non-sorted attributes)

Dense index: every unique value of the index attribute(s) has a 
direct pointer to itself. 

Sparse index: Not every value of the index attribute(s) has a 
direct pointer. Records are sorted and the specific record can be found 
by using the pointers to close values. (only clusted indexes can use 
Sparse index). 

Multi-level indexes: 
if an index is too large to be loaded entirely in memory, 
make another sparse index of the index records. (Forms a tree structure). 
Keep the root of the tree in memory at all times.

#### B+ Balanced Tree
One type of balanced tree, the lengths of all paths from root to  
leaf nodes are all equal. (leaf nodes are all in the same level)

#### Hashing
A hash function which takes Search key value as input and returns 
an address in memory.

An ideal hash function for database storage has the following properties:
- Deterministic behavior (same search key sent in twice MUST 
yield same output).
- Yields an answer for all possible search keys.
- Distributes search keys across the allowed storage space in 
as uniform a manner as possible.
- Quick to calculate.

##### Hashing Overflow
![Hashing_Overflow](../docs/assets/hashing_overflow.png)

#### Clustered vs Hashing
![ClusteredVsHashing](../docs/assets/clusteredVsHashing.png)


## Week 6 Transaction Management

![DatabaseACID](../docs//assets/database_ACID.png)

![TransactionManagers](../docs/assets/transaction_managers.png)

## Week 10 NoSQL

![NoSQL_vs_Relational](../docs/assets/noSQLvsRelational.png)

![BASE_properties](../docs/assets/baseProperties.png)
