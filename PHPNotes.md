# PHP Notes

### Password Hashing
```injectablephp
$passwordHash = password_hash($password, PASSWORD_DEFAULT);
```


## Input

### Password Input
```injectablephp
<input type="password" name="password"
```

Credentials should be stored outside www or htdocs folder, so that user cannot access it.
Also, ideally credentials should not be stored in the repository.

## SQL Injection
Example: data loss
Website asks for email using input field. •Hacker inputs:
```injectablephp
 x'; DROP TABLE members; --';
```
Sent to database as SQL query:
```MySQL
SELECT email, passwd, login_idFROM members WHERE email = 'x'; DROP TABLE members; --';
```

## Denial of Service (DoS) Injection
