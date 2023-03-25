# Event Ticket Reservation Automation System (https://www.eventim.bg/bg/)
## The project is an event ticket reservation automation system that aims to simplify and streamline the event ticket booking process. The system is designed to work based on predefined user preferences. The system will automatically reserve tickets for the user and send a confirmation email once the reservation is complete.

### The system will consist of several components:

- User Interface:
The system will have a user interface where users can enter their preferences, such as event type, date, and time. They can also specify the number of tickets they require and the price range they are willing to pay.

- Event Database: The system will use an event database that contains information about various events. The database will include details such as the name of the event, location, date, time, price, and availability.

- Reservation Engine: The system's booking engine will search the event database based on the user's preferences and available days. The reservation engine will also check the availability of tickets and the user's specified price range. Once it finds a suitable event, it will automatically book tickets for the user.

- Confirmation Email: Once the reservation is complete, the system will send a confirmation email to the user. The email will contain details about the event, the tickets booked, and the payment confirmation.

- The system's main objective is to provide a hassle-free and efficient way of reservation tickets for events. By automating the process, users can save time and effort, and they can be sure that they will get the best available tickets based on their preferences and budget.

Upcoming feature:
- Payment Gateway
- Work in background
____
## Architecture for the Eventim Ticket Reservatione system:
```
         +-----------------------------------+
         |             Web Browser           |
         +-----------------------------------+
                   | HTTP Requests
                   v
         +-----------------------------------+
         |      GUI / Web Application        |
         +-----------------------------------+
                   | Interacts with:
                   | - Database
                   | - Payment Processor (optional)
                   | - AI Bot for Seats
                   | - AI Bot for Event Recommendations
                   v
         +-----------------------------------+
         |            Database               |
         +-----------------------------------+
                   | Stores data related to:
                   | - Users
                   | - Events
                   | - Reservations
                   v
         +-----------------------------------+
         |           Backend GUI             |
         +-----------------------------------+
                   | Provides a UI for managing events and reservations
                   v
        +------------------|         |-----------------------|
        | AI Bot for Seat  |         | AI Bot for Event      |
        | Selection        |<------->|                       |
        +------------------|         |-----------------------+

```