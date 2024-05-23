-- Lists all privileges of the users user_0d_1 and user_0d_2
SELECT grantee, privilege_type 
FROM information_schema.user_privileges 
WHERE grantee = "'user_0d_1'@'localhost'"
OR grantee = "'user_0d_2'@'localhost'";
