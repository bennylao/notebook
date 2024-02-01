# Prisma Notes

## Model

Every record of a model must be uniquely identifiable.

You must define at least one of the following attributes per model:

- `@unique`
- `@@unique`
- `@id`
- `@@id`

### `@id`

Corresponding database type is `PRIMARY KEY`.

Arguments:
- `map`
- `length`
- `sort`
- `clustered`

It can be annotated with a `@default()` value that uses functions to auto-generate an ID:

- `autoincrement()`
    - Compatible with `Int` on most databases, implemented on the database-level.
    - Equivalent to `AUTO_INCREMENT` on MySQL and `SERIAL` on PostgreSQL

```prisma
model User {
  id   Int    @id @default(autoincrement())
  name String
}
```

- `uuid()`
    - Generate a globally unique identifier based on the UUID where UUID is a 128-bit label
    - Probability of getting duplicate label is nearly zero
    - Label is too big and it takes up too much space in the URL

```prisma
model User {
  id   String @id @default(uuid())
  name String
}
```

- `cuid()`
    - Shorter than UUID, but the chances for collisions are still extremely slim

```prisma
model User {
  id   String @id @default(cuid())
  name String
}
```

### `@@id`
This is composite primary key

```prisma
model User {
  firstName String
  lastName  String
  email     String  @unique
  isAdmin   Boolean @default(false)

  @@id([firstName, lastName, isAdmin])
}
```

### `@unique`
Defines a unique constraint for this field.

```prisma
model User {
  id    Int     @id @default(autoincrement())
  email String? @unique
  name  String
}
```

### `@@unique`
Defines a compound unique constraint for the specified fields.

### `[]` modifier

- Cannot be optional (`Post[]?`)
- Only supported in the data model if your database natively supports them.
Currently, only PostgreSQL, CockroachDB and MongoDB support array.

```prisma
model User {
  id             Int      @id @default(autoincrement())
  favoriteColors String[]
}

// scalar list with a default value
model User {
  id             Int      @id @default(autoincrement())
  favoriteColors String[] @default(["red", "blue", "green"])
}
```

### `@default`

Defines a default value for a field.

Default values can be a static value (4, "hello") or one of the following functions:

- `autoincrement()`
- `sequence()` (CockroachDB only)
- `dbgenerated()`
- `cuid()`
- `uuid()`
- `now()`

### `?` modifier
- Makes a field optional
- Cannot be used with a list field

```prisma
model User {
  id   Int     @id @default(autoincrement())
  name String?
}
```

### `@@index`

Defines an index in the database

```prisma
model Post {
  id      Int     @id @default(autoincrement())
  title   String
  content String?

  @@index([title])
}
```

```prisma
model Post {
  id      Int     @id @default(autoincrement())
  title   String
  content String?

  @@index(fields: [title, content], name: "main_index")
}
```

### `@relation`

- Corresponding database types are `FOREIGN KEY` / `REFERENCE`
- 

Arguments:

- `name`
- `fields`
- `references`
- `map`
- `onUpdate`
- `onDelete`

```prisma
@relation(name: "UserOnPost", references: [id])
```

```prisma
@relation(_ name: String?, fields: FieldReference[]?, references: FieldReference[]?, onDelete: ReferentialAction?, onUpdate: ReferentialAction?, map: String?)
```

### `@map`
Maps a field name or enum value from the Prisma schema to a column or document field with a different name in the database. 
If you do not use @map, the Prisma field name matches the column name or document field name exactly.

```prisma
model User {
  id        Int    @id @default(autoincrement())
  firstName String @map("first_name")
}
```

### `@@map`
Maps the Prisma schema model name to a table (relational databases) or collection (MongoDB) with a different name, 
or an enum name to a different underlying enum in the database. 
If you do not use @@map, the model name matches the table (relational databases) or collection (MongoDB) name exactly.

```prisma
model User {
  id   Int    @id @default(autoincrement())
  name String

  @@map("users")
}
```

### `@updatedAt`
Automatically stores the time when a record was last updated. If you do not supply a time yourself, 
Prisma Client will automatically set the value for fields with this attribute.

```prisma
model Post {
  id        String   @id
  updatedAt DateTime @updatedAt
}
```

### `@ignore`
Add @ignore to a field that you want to exclude from Prisma Client (for example, a field that you do not want Prisma users to update). 
Ignored fields are excluded from the generated Prisma Client. 
The model's create method is disabled when doing this for required fields with no @default (because the database cannot create an entry without that data).

```prisma
model User {
  id    Int    @id
  name  String
  email String @ignore // this field will be excluded
}
```

### `@@ignore`
Add @@ignore to a model that you want to exclude from Prisma Client (for example, a model that you do not want Prisma users to update). 
Ignored models are excluded from the generated Prisma Client.

```prisma
/// The underlying table does not contain a valid unique identifier and can therefore currently not be handled by Prisma Client.
model Post {
  id       Int  @default(autoincrement()) // no unique identifier
  author   User @relation(fields: [authorId], references: [id])
  authorId Int

  @@ignore
}
```

### `@@schema`
To use this attribute, you must have the multiSchema preview feature enabled. Multiple database schema support is 
currently available with the PostgreSQL, CockroachDB, and SQL Server connectors.

Add `@@schema` to a model to specify which schema in your database should contain the table associated with that model.

```prisma
generator client {
  provider        = "prisma-client-js"
  previewFeatures = ["multiSchema"]
}

datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
  schemas  = ["auth"]
}

model User {
  id   Int    @id @default(autoincrement())
  name String

  @@schema("auth")
}
```

### `enum`

- Enums are natively supported by PostgreSQL and MySQL
- Enum names must start with a letter (they are typically spelled in PascalCase)
- Enums must use the singular form (e.g. `Role` instead of `role`, `roles` or `Roles`).
- Must adhere to the following regular expression: `[A-Za-z][A-Za-z0-9_]*`

```prisma
enum Role {
  USER
  ADMIN
}

model User {
  id   Int  @id @default(autoincrement())
  role Role @default(USER)
}
```

