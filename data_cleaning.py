
import os, sys

def main():

    data_out = "Couple,Score,Dance,Music,Result,Series,Week\n"
    for season_index in range(1, 19):
        f = "season{}.csv".format(season_index)
        # extra column in s9 and s12
        with open(f, "r") as file:
            week_index = 0
            
            for line in file:
                
                week_bool = line.startswith("Week") or line.startswith("\"Week")
                
                if week_bool:
                    week_index += 1
                
                if (not(week_bool) and 
                    line.split(",")[1] != "" and
                    "\"" in line.split(",")[1] and 
                    len(line.split(",")[2]) > 0
                ):
                    
                    data_out += line.strip() + ",{}, {}\n".format(season_index, week_index)
    
    with open("results_cleaned.csv", "w") as file:
        file.write(data_out)
    
    return 


if __name__ == "__main__":
    
    main()