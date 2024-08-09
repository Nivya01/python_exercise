class Details:


    def total(self):
        """
        Calculates and prints the total score across all subjects.

        This method sums up the scores for the subjects Tamil, English, Maths, Science, and Social, 
        and prints the total.

        Attributes:
            self.tamil (int or float): The score in Tamil.
            self.english (int or float): The score in English.
            self.maths (int or float): The score in Maths.
            self.science (int or float): The score in Science.
            self.social (int or float): The score in Social.

        Returns:
            None
        """
        print(self.tamil + self.english + self.maths + self.science + self.social)


# class Details ends here


# instantiating details class for student 1
student1 = Details()

# setting properties for student 1
student1.name = 'Ramya'
student1.tamil = 69
student1.english = 89
student1.maths = 59
student1.science = 69
student1.social = 99

# instantiating details class for student 2
student2 = Details()

# setting properties for student 2
student2.name = 'Priya'
student2.tamil = 88
student2.english = 77
student2.maths = 55
student2.science = 66
student2.social = 44

    

# invoke total function for student 1 and 2
student1.total()
student2.total()