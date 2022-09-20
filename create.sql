-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2021-12-05 19:28:48.192

-- tables
-- Table: Business
CREATE TABLE Business (
    id int  NOT NULL,
    name text  NOT NULL,
    price_range int  NOT NULL,
    cuisine text  NOT NULL,
    CONSTRAINT Business_pk PRIMARY KEY (id)
);

-- Table: Customer
CREATE TABLE Customer (
    id int  NOT NULL,
    name text  NOT NULL,
    points int  NOT NULL,
    CONSTRAINT Customer_pk PRIMARY KEY (id)
);

-- Table: DashPassUser
CREATE TABLE DashPassUser (
    Customer_id int  NOT NULL,
    CONSTRAINT DashPassUser_pk PRIMARY KEY (Customer_id)
);

-- Table: Delivery
CREATE TABLE Delivery (
    Business_id int  NOT NULL,
    Driver_id int  NOT NULL,
    CONSTRAINT Delivery_pk PRIMARY KEY (Business_id,Driver_id)
);

-- Table: Demand
CREATE TABLE Demand (
    Order_id int  NOT NULL,
    MenuItem_id int  NOT NULL,
    CONSTRAINT Demand_pk PRIMARY KEY (Order_id,MenuItem_id)
);

-- Table: Discount
CREATE TABLE Discount (
    id int  NOT NULL,
    discount_pct decimal  NOT NULL,
    is_dashpass boolean  NOT NULL,
    Business_id int  NOT NULL,
    CONSTRAINT Discount_pk PRIMARY KEY (id)
);

-- Table: Driver
CREATE TABLE Driver (
    id int  NOT NULL,
    name text  NOT NULL,
    CONSTRAINT Driver_pk PRIMARY KEY (id)
);

-- Table: Exchange
CREATE TABLE Exchange (
    Customer_id int  NOT NULL,
    Reward_id int  NOT NULL,
    CONSTRAINT Exchange_pk PRIMARY KEY (Customer_id,Reward_id)
);

-- Table: MenuItem
CREATE TABLE MenuItem (
    id int  NOT NULL,
    name text  NOT NULL,
    category text  NOT NULL,
    price decimal  NOT NULL,
    Business_id int  NOT NULL,
    CONSTRAINT MenuItem_pk PRIMARY KEY (id)
);

-- Table: NonDashPassUser
CREATE TABLE NonDashPassUser (
    Customer_id int  NOT NULL,
    CONSTRAINT NonDashPassUser_pk PRIMARY KEY (Customer_id)
);

-- Table: Order
CREATE TABLE "Order" (
    id int  NOT NULL,
    date date  NOT NULL,
    price decimal  NOT NULL,
    Customer_id int  NOT NULL,
    Business_id int  NOT NULL,
    Driver_id int  NOT NULL,
    Discount_id int  NOT NULL,
    rating int  DEFAULT NULL,
    CONSTRAINT Order_pk PRIMARY KEY (id)
);

-- Table: Review
CREATE TABLE Review (
    id int  NOT NULL,
    rating decimal  NOT NULL,
    comment text  NOT NULL,
    Customer_id int  NOT NULL,
    Business_id int  NOT NULL,
    CONSTRAINT Review_pk PRIMARY KEY (id)
);

-- Table: Reward
CREATE TABLE Reward (
    id int  NOT NULL,
    reward text  NOT NULL,
    points_needed int  NOT NULL,
    CONSTRAINT Reward_pk PRIMARY KEY (id)
);

-- Table: Use
CREATE TABLE Use (
    Discount_id int  NOT NULL,
    Customer_id int  NOT NULL,
    CONSTRAINT Use_pk PRIMARY KEY (Discount_id,Customer_id)
);

-- foreign keys
-- Reference: BusinessDelivery_Business (table: Delivery)
ALTER TABLE Delivery ADD CONSTRAINT BusinessDelivery_Business
    FOREIGN KEY (Business_id)
    REFERENCES Business (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: BusinessDelivery_Drivers (table: Delivery)
ALTER TABLE Delivery ADD CONSTRAINT BusinessDelivery_Drivers
    FOREIGN KEY (Driver_id)
    REFERENCES Driver (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Coupons_Business (table: Discount)
ALTER TABLE Discount ADD CONSTRAINT Coupons_Business
    FOREIGN KEY (Business_id)
    REFERENCES Business (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: DashPass_Customers (table: DashPassUser)
ALTER TABLE DashPassUser ADD CONSTRAINT DashPass_Customers
    FOREIGN KEY (Customer_id)
    REFERENCES Customer (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Demand_Order (table: Demand)
ALTER TABLE Demand ADD CONSTRAINT Demand_Order
    FOREIGN KEY (Order_id)
    REFERENCES "Order" (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Demands_Menu_Item (table: Demand)
ALTER TABLE Demand ADD CONSTRAINT Demands_Menu_Item
    FOREIGN KEY (MenuItem_id)
    REFERENCES MenuItem (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Exchange_Customer (table: Exchange)
ALTER TABLE Exchange ADD CONSTRAINT Exchange_Customer
    FOREIGN KEY (Customer_id)
    REFERENCES Customer (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Exchange_Reward (table: Exchange)
ALTER TABLE Exchange ADD CONSTRAINT Exchange_Reward
    FOREIGN KEY (Reward_id)
    REFERENCES Reward (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Menu_Item_Business (table: MenuItem)
ALTER TABLE MenuItem ADD CONSTRAINT Menu_Item_Business
    FOREIGN KEY (Business_id)
    REFERENCES Business (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: NonDashPassUser_Customers (table: NonDashPassUser)
ALTER TABLE NonDashPassUser ADD CONSTRAINT NonDashPassUser_Customers
    FOREIGN KEY (Customer_id)
    REFERENCES Customer (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Order_Business (table: Order)
ALTER TABLE "Order" ADD CONSTRAINT Order_Business
    FOREIGN KEY (Business_id)
    REFERENCES Business (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Order_Customers (table: Order)
ALTER TABLE "Order" ADD CONSTRAINT Order_Customers
    FOREIGN KEY (Customer_id)
    REFERENCES Customer (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Order_Discount (table: Order)
ALTER TABLE "Order" ADD CONSTRAINT Order_Discount
    FOREIGN KEY (Discount_id)
    REFERENCES Discount (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Order_Drivers (table: Order)
ALTER TABLE "Order" ADD CONSTRAINT Order_Drivers
    FOREIGN KEY (Driver_id)
    REFERENCES Driver (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Reviews_Business (table: Review)
ALTER TABLE Review ADD CONSTRAINT Reviews_Business
    FOREIGN KEY (Business_id)
    REFERENCES Business (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Reviews_Customers (table: Review)
ALTER TABLE Review ADD CONSTRAINT Reviews_Customers
    FOREIGN KEY (Customer_id)
    REFERENCES Customer (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Use_Coupons (table: Use)
ALTER TABLE Use ADD CONSTRAINT Use_Coupons
    FOREIGN KEY (Discount_id)
    REFERENCES Discount (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Use_Customers (table: Use)
ALTER TABLE Use ADD CONSTRAINT Use_Customers
    FOREIGN KEY (Customer_id)
    REFERENCES Customer (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- End of file.

