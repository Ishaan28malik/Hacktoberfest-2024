######################################
#  ____ ____  _____ ____ _    ______  ____ ______ ____ ___  ____       ____   ____ ______   ___ _____
# |    |    \|     |    | |  |      |/    |      |    /   \|    \     |    \ /    |      | /  _/ ___/
#  |  ||  _  |   __||  || |  |      |  o  |      ||  |     |  _  |    |  D  |  o  |      |/  [(   \_ 
#  |  ||  |  |  |_  |  || |__|_|  |_|     |_|  |_||  |  O  |  |  |    |    /|     |_|  |_|    _\__  |
#  |  ||  |  |   _] |  ||     ||  | |  _  | |  |  |  |     |  |  |    |    \|  _  | |  | |   [_/  \ |
#  |  ||  |  |  |   |  ||     ||  | |  |  | |  |  |  |     |  |  |    |  .  |  |  | |  | |     \    |
# |____|__|__|__|  |____|_____||__| |__|__| |__| |____\___/|__|__|    |__|\_|__|__| |__| |_____|\___|
#                                                                               ~Infiltation Rates~
#                                                                               by joshuqa aka Roni
# GitHub: https://github.com/nobalpha
# 
# -Excel data from KHAS University
######################################

#' this is a silly function
#' @param dataset takes a list-type object
#' @param countries takes a vector-type object
#' @param min minimum y limit (default=0)
#' @param max maximum y limit (default=100)
#' @return NULL
country_plotter <-function(dataset=NA, countries=NA, min=0L, max=100L) {
  # Checking if input formats are as requested
  if (!(is.list(dataset) && is.vector(countries))) { # Dataset must be a list and countries must be a vector
    message("Please enter like asked format...")
    return()
  }
  ######################################
  
  # Calculating the delta year
  start<-as.numeric(colnames(dataset)[2])
  stop<-as.numeric(colnames(dataset)[length(dataset)])
  years = start:stop 
  ######################################
  
  maxcolor = c(palette(rainbow(length(countries)+1))) # Gather color range for plot
  print(countries)
  temp<-1L # Setting a dummy for iterating simultaneously over maxcolor
  
  # Names and colors vector for labeling
  names = c() 
  color_history = c()
  ######################################
  # Plot function details:
  # as.numeric(dataset[dataset$`Country Name`==countries[1],-1]) -> Gets the row (without Country Name) where Country Name column is the first country
  #                                                              -> Turns all the data to Numeric format
  #                                                              -> This is a just a pre-plotter function to initialize the main body of the plot
  #
  plot(years, as.numeric(dataset[dataset$`Country Name`==countries[1],-1]),type="l", lwd=3, xlab="Years", ylab="Infiltation Rates", main="Infiltation Rates per year and country", ylim=c(min,max))
  ######################################
  
  for (country in countries) { # Iterates through the country_list
    
    buff<-dataset[dataset$`Country Name`==country,] # Takes the matching country row to the buffer
    
    lines(years, as.numeric(buff[-1]), col=maxcolor[temp], lwd=3, type="l", ylim=c(min,max)) # Adds a new line to the main body
    
    color_history = c(color_history, maxcolor[temp]) # Colors_history gets updated
    
    names = c(names, buff[1]) # Names also gets updated
    
    temp = temp + 1L  # To maintain synchronization, increments dummy by one
  }
  
  legend("topright", legend=names, lwd=3, col=color_history, text.col="black") # After all, legend is getting placed to the topright corner with all of the information
  
  return() # It returns nothing to be able to pass the current while loop
}

# First function which'll be executed, to check whether required packages are installed or not 
setRequirements <-function(){ 
  
  tryCatch({
    # Getting RStudioAPI to able to pwd
    install.packages("rstudioapi")
    library("rstudioapi")
    ######################################
    
    message("[OK] RStudioAPI package imported sucessfully...")
    
    setwd(dirname(rstudioapi::getSourceEditorContext()$path)) # Setting working directory
    
  }, warning= function(w){
    
    warning("[Warning] ", w)
    
  }, error= function(err){
    
    stop("[Error] ", err)
    
  })
  
  Sys.sleep(3)
  
  tryCatch({
    # Getting readxl to read excel-like files
    install.packages("readxl")
    library("readxl")
    ######################################
    
    message("[OK] readxl package imported sucessfully...")
    
    xfile <<- readxl::read_xls(file.choose()) # Reading the chose xls to the global variable file
    
  }, warning= function(w){
    
    warning("[Warning] ", w)
    
  }, error= function(err){
    
    stop("[Error] ", err)
    
  })
}

country_list = ""
message("~Infiltation Rates~\n\tby joshuqa aka Roni\n\t\tGitHub: https://github.com/nobalpha\n\t\t\t-Excel data from KHAS University")

while(TRUE) {
  
  country_list = readline("Write the name(s) of the country(ies) that you want to plot their infiltation rate (with spaces).\nOr type [I] for install dependencies...\nElse just type [Q] for quit...\nInput: ")
  if (toupper(trimws(country_list))=="I") {
    message("Installing the packages: readxl & rstudioapi")
    setRequirements()
  } else if(toupper(trimws(country_list))=="Q") {
    break
  }
  country_list = unlist(strsplit(country_list, " "))
  country_plotter(xfile, country_list)
}

