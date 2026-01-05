from pyscript import document

def compute_average(event):
        # Get the input values and convert to float
        
            score1 = float(document.getElementById("score1").value)
            score2 = float(document.getElementById("score2").value)

            # Compute for the average
            average = (score1 + score2) / 2

            # Determine if pass/fail
            if average >= 75:
                result = "Pass" 
            else:
                result = "Fail"

            # Display the result
            document.getElementById("average").innerText = "Average: " + str(round(average, 2))
            document.getElementById("result").innerText = "Result: " + result

            