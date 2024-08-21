
-- Add Index to Transactions for faster lookup by user_id
CREATE INDEX idx_user_id ON transactions(user_id);

-- Optimize a query by using the index
EXPLAIN SELECT * FROM transactions WHERE user_id = 1;
