CREATE TABLE "wires" (
  "wire_id" serial PRIMARY KEY,
  "wire_num" varchar,
  "wire_data" integer
);

CREATE TABLE "contacts" (
  "cont_id" serial PRIMARY KEY,
  "pin_id" integer,
  "num" integer,
  "x" float,
  "y" float,
  "z" float,
  "angle" float,
  "con_id" integer
);

CREATE TABLE "connections" (
  "con_id" serial PRIMARY KEY,
  "con_name" varchar,
  "im_id" integer,
  "board" integer,
  "quan_pins" integer
);

CREATE TABLE "imitator" (
  "im_id" serial PRIMARY KEY,
  "im_type" integer,
  "x_center" float,
  "y_center" float,
  "angle" float
);

CREATE TABLE "knots" (
  "knot_id" serial PRIMARY KEY,
  "x" float,
  "y" float,
  "z" float,
  "angle" float
);

CREATE TABLE "wire_data" (
  "id_data" serial PRIMARY KEY,
  "type" varchar,
  "diameter" integer
);

CREATE TABLE "boards" (
  "id_board" serial PRIMARY KEY,
  "name_board" varchar
);

CREATE TABLE "con_wire" (
  "wire_id" integer,
  "con_beg_id" integer,
  "con_end_id" integer
);

CREATE TABLE "wire_knots" (
  "wire_id" integer,
  "knot_num" integer,
  "knot_id" integer
);

CREATE TABLE "im_type" (
  "im_type_id" serial PRIMARY KEY,
  "name" varchar,
  "quan_pins" integer,
  "height" float,
  "width" float
);

CREATE TABLE "pins" (
  "pin_id" serial PRIMARY KEY,
  "im_id" integer,
  "num" integer,
  "x" float,
  "y" float
);

ALTER TABLE "pins" ADD FOREIGN KEY ("pin_id") REFERENCES "contacts" ("pin_id");

ALTER TABLE "contacts" ADD FOREIGN KEY ("con_id") REFERENCES "connections" ("con_id");

ALTER TABLE "connections" ADD FOREIGN KEY ("im_id") REFERENCES "imitator" ("im_id");

ALTER TABLE "imitator" ADD FOREIGN KEY ("im_type") REFERENCES "im_type" ("im_type_id");

ALTER TABLE "wires" ADD FOREIGN KEY ("wire_data") REFERENCES "wire_data" ("id_data");

ALTER TABLE "connections" ADD FOREIGN KEY ("board") REFERENCES "boards" ("id_board");

ALTER TABLE "con_wire" ADD FOREIGN KEY ("wire_id") REFERENCES "wires" ("wire_id");

ALTER TABLE "con_wire" ADD FOREIGN KEY ("con_beg_id") REFERENCES "contacts" ("cont_id");

ALTER TABLE "con_wire" ADD FOREIGN KEY ("con_end_id") REFERENCES "contacts" ("cont_id");

ALTER TABLE "wire_knots" ADD FOREIGN KEY ("wire_id") REFERENCES "wires" ("wire_id");

ALTER TABLE "wire_knots" ADD FOREIGN KEY ("knot_id") REFERENCES "knots" ("knot_id");

ALTER TABLE "pins" ADD FOREIGN KEY ("im_id") REFERENCES "im_type" ("im_type_id");
