#🎬 Project 17: Movie Ticket Booking System — Create a movie booking system to show movies, select a movie and seats, calculate the total ticket price, and confirm or cancel the booking.

movies = {
    "Avengers": 200,
    "Avatar": 250,
    "Titanic": 150
}

def show_movie():

    while True:

      #show movies
      print(movies)

      #select movies and seats 

      show_mov=input("enter a movie you want to watch:").title()
      if show_mov in movies:
         seats=int(input("how many seats do you want to book:"))

         total=seats*movies[show_mov]
         print("total ticket price is:",total)

         ##confirm or cancel the booking
         booking=input("Do you want to confirm your booking? (yes/No):")
         if booking=="yes":
                 print("booking confirmed")
         else:
                 print("booking cancelled")  

      else:
         
         print("movie not found")  

         #continue booking

      other_booking=input("Do you want to book another ticket? (yes/no) ")
      if other_booking=="yes":
         continue
      else:
         print("Thanku  for booking!")       
         break

show_movie() 