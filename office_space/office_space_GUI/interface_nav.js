// Dummy Data Objects

// 10 Locations (L1-L10, name is same as code (see below). Use region as location description)

// 5 Buildings (B1-B5, name UST list or same as code. Use `This is ${building_name} located at ${location_name}.`

// 5 Floors (Fl-F5, if no floor name use "floor(number)", "level", "piso", or "mezzanine")

// 5 Seats (seat_number is S1-5 + ${floor_code} + ${building_code} + ${location_code}. 
// seat_type options are corner, cubicle, conference, desk (normal), and manager.

// 4 assigned employees (have id, pswd, name, email and user role which are ADMIN, LOCATION_ANCHOR, BUILDING_ANCHOR, FLOOR_ANCHOR, or null. 

// 1 unassigned employee (for demo, will be sample person assigned a seat using the site.)

// From Roster--> Employee Id, Employee Name, Seat Number  (assuming employee id is "email_id")
// From database variables --> id, password, role
//         1234, John Doe, L1B2F3 --> 00001, UST@One1, FLOOR_ANCHOR
//         4321, Juana Perez, L48B5F1 --> 00056, My$Job98, LOCATION_ANCHOR
//         2413, Jose Publico, L15B3F2 --> 00987, Let5Go!!, ADMIN
//         3142, Hanako Yamada, L39B3F2 --> 02431, 1stJob=$, null

// New employee for demo:
// 	4132, Fulan AlFulani, L2____ --> 27510, 4Demo&Td, BUILDING_ANCHOR

// Database groupings (Use as [] of {} lists)

// const Locations = {
// location_name {
// location_code:"";
// location_description:"";
// location_city:"";
// location_country:"";
// }
// }

// const Buildings ={
// building_name {
// building_code:"";
// building_description:"";
// location_code:"";
// }
// }

// const Floors = {
// floor_name {
// floor_code:"";
// floor_description:"";
// location_code:"";
// building_code:"";
// } 

// const Users = {
// user {
// id:"";
// password:"";
// employee_name:"";
// email_id:"";
// location_code:"";
// building_code:"";
// floor_code:"";
// user_role:"";
// }
// }

// const Seats = {
// seat {
// seat_number:"";
// seat_type:"";}
// location_code:"";
// building_code:"";
// floor_code:"";
// employee_id:"";
// }
// }

// All Database Variables (16) Convert all html ids to match

// id
// employee_id	(user_id, employee_id, id are the same?)
// password
// employee_name
// email_id
// user_role
// seat_number
// seat_type
// floor_code
// floor_description
// building_code
// building_description
// location_code
// location_description
// location_city
// location_country

// Use these to populate all of the user pages/interfaces. Use it to create the search queries. 
// Rename js variables and html ids and classes.

//UST Site locations (Street address and phone numbers are not needed.
//Remove in object conversion.)

// MEXICO
// Guadalajara
// Loft 5, Edificio Central Interior #2, Unidad Privativa 117, Boulevard Puerta de Hierro 4965, Col. Puerta de Hierro, Zapopan, Jalisco, C.P. 45116
// Phone +52 472 500 1028

// MEXICO
// Leon
// Plaza de La Paz, No. 102, Suite 1201 & 1101, COL.GTO Puerto Interior, Silao, Leon-36275
// Phone +52 472 500 1019

// USA
// Atlanta GA
// 1355 Windward Concourse, Suite 400, Alpharetta GA 30005
// Phone +1 949 716 8757

// USA
// Sidney NE
// 812 13th Avenue, Sidney NE 69162
// Phone +1 949 716 8757

// SPAIN
// Barcelona
// Plaça d’Ernest Lluch i Martín, 08019 Barcelona

// SPAIN
// Madrid
// Santa Leonor 65, Edificio G, 20043 Madrid

// MALAYSIA
// Cyberjaya
// 4808-3A-21, CBD Perdana 2, Jalan Perdana, CBD Perdana Cyber 12, 63000 Cyberjaya

// MALAYSIA
// Penang
// Level 2, Mini Circuits Building 3, Technoplex Plot 10, Phase IV, 1Bayan Lepas Industrial Zone, 11900 Penang
// Phone +604 638 6550

// INDIA
// Bangalore
// 14th Floor, Tower B, Prestige Shantiniketan, Whitefield Bangalore - 560 066
// Phone +91 471 404 0000

// INDIA
// Delhi
// 5th Floor, Tower – C, Plot no - 2B, INDIA GLYCOL Building, Sector 126, Noida 201304
// Phone +91 471 404 0000