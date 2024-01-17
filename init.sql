CREATE TABLE public.house_prices (
    id SERIAL PRIMARY KEY,
    property_type VARCHAR(100),
    price INTEGER,
    location VARCHAR(100),
    city VARCHAR(100),
    baths INTEGER,
    purpose VARCHAR(100),
    bedrooms INTEGER,
    Area_in_Marla FLOAT
);

\COPY public.house_prices (id, property_type, price, location, city, baths, purpose, bedrooms, Area_in_Marla)
FROM '/tmp/house_prices.csv' DELIMITER ',' CSV HEADER;
