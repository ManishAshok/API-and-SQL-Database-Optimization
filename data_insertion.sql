
-- Insert sample users
INSERT INTO users (username, email) VALUES
('john_doe', 'john@example.com'),
('jane_smith', 'jane@example.com');

-- Insert sample transactions
INSERT INTO transactions (user_id, amount) VALUES
(1, 100.50),
(2, 200.75),
(1, 50.00);

-- Insert sample logs
INSERT INTO logs (log_message) VALUES
('User john_doe created'),
('Transaction 100.50 processed for user 1'),
('User jane_smith created');
