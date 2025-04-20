CREATE TABLE IF NOT EXISTS Transaction (
            id SERIAL PRIMARY KEY,
            Transcation_Date DATE, 
            Post_Date DATE,
            Description TEXT,
            Category TEXT,
            Type text,
            Amount FLOAT,
            Memo TEXT
);
