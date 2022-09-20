\c postgres

DROP DATABASE IF EXISTS doordash;

CREATE database doordash;
\c doordash

DROP TABLE IF EXISTS Business CASCADE;
DROP TABLE IF EXISTS Customer CASCADE;
DROP TABLE IF EXISTS DashPassUser CASCADE;
DROP TABLE IF EXISTS Delivery CASCADE;
DROP TABLE IF EXISTS Demand CASCADE;
DROP TABLE IF EXISTS Discount CASCADE;
DROP TABLE IF EXISTS Driver CASCADE;
DROP TABLE IF EXISTS MenuItem CASCADE;
DROP TABLE IF EXISTS NonDashPassUser CASCADE;
DROP TABLE IF EXISTS "Order" CASCADE;
DROP TABLE IF EXISTS Review CASCADE;
DROP TABLE IF EXISTS Use CASCADE;
DROP TABLE IF EXISTS Reward CASCADE;
DROP TABLE IF EXISTS Exchange CASCADE;


\i create.SQL


\copy Customer(id, name, points) FROM 'Customer.csv'  csv header
\copy DashPassUser(customer_id) FROM 'DashPassUser.csv'  csv header
\copy NonDashPassUser(customer_id) FROM 'NonDashPassUser.csv'  csv header
\copy Driver(id, name) FROM 'Driver.csv'  csv header
\copy Business(id, name, price_range, cuisine) FROM 'Business.csv'  csv header
\copy Discount(id, discount_pct, is_dashpass, business_id) FROM 'Discount.csv'  csv header
\copy "Order"(id, date, price, customer_id, business_id, driver_id, discount_id, rating) FROM 'Order.csv'  csv header
\copy MenuItem(id, name, category, price, business_id) FROM 'MenuItem.csv'  csv header
\copy Review(id, rating, comment, customer_id, business_id) FROM 'Review.csv'  csv header
\copy Use(customer_id, discount_id) FROM 'Use.csv'  csv header
\copy Delivery(business_id, driver_id) FROM 'Delivery.csv'  csv header
\copy Demand(order_id, menuItem_id) FROM 'Demand.csv'  csv header
\copy Reward(id, reward, points_needed) FROM 'Reward.csv'  csv header
\copy Exchange(customer_id, reward_id) FROM 'Exchange.csv'  csv header


-- ============================================================
  
