# Title: Generating a Monopoly Board Probability Heatmap
# Author: Kyriacos Rouvas
# Date: 14/07/2021


#Loading libraries
library(ggplot2)
library(colorRamps)


#Declaring probability list
probs <- c(0.01944, 0.01954, 0.01963, 0.01980, 0.01936, 0.01918, 0.01910, 0.01901, 0.01897, 0.01891,
           0.17175, 0.01895, 0.01994, 0.02112, 0.02236, 0.02344, 0.02481, 0.02626, 0.02555, 0.02509, 
           0.02467, 0.02421, 0.02385, 0.02339, 0.02396, 0.02412, 0.02422, 0.02411, 0.02387, 0.02368, 
           0.02500, 0.02350, 0.02271, 0.02208, 0.02139, 0.02063, 0.01976, 0.01894, 0.01921, 0.01933)

#Preparing color vector for heatmap
fills <- c()

ord <- sort(probs, decreasing = FALSE)

pal <- heat.colors(length(ord))


for (i in probs) {
  fills <- append(fills, pal[match(i, ord)])
}


#Setting up dataframe
df <- data.frame(number <- 0:39,
                 fill <- c(fills[1:30], "white", fills[32:40]),
                 color <- c(rep("#000000", 40)))

#Defining dimensions and coordinates of board tiles
x.pos <- c(45.75, 40.5, 36.5, 32.5, 28.5, 24.5, 20.5, 16.5, 12.5, 8.5, 
           3.25, 3.25, 3.25, 3.25, 3.25, 3.25, 3.25, 3.25, 3.25, 3.25,
           3.25, 8.5, 12.5, 16.5, 20.5, 24.5, 28.5, 32.5, 36.5, 40.5,
           45.75, 45.75, 45.75, 45.75, 45.75, 45.75, 45.75, 45.75, 45.75, 45.75)

y.pos <- c(3.25, 3.25, 3.25, 3.25, 3.25, 3.25, 3.25, 3.25, 3.25, 3.25,
           3.25, 8.5, 12.5, 16.5, 20.5, 24.5, 28.5, 32.5, 36.5, 40.5,
           45.75, 45.75, 45.75, 45.75, 45.75, 45.75, 45.75, 45.75, 45.75, 45.75,
           45.75, 40.5, 36.5, 32.5, 28.5, 24.5, 20.5, 16.5, 12.5, 8.5)

w <- c(6.5, 4, 4, 4, 4, 4, 4, 4, 4, 4,
       6.5, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5,
       6.5, 4, 4, 4, 4, 4, 4, 4, 4, 4,
       6.5, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5)

h <- c(6.5, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5,
       6.5, 4, 4, 4, 4, 4, 4, 4, 4, 4,
       6.5, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5,
       6.5, 4, 4, 4, 4, 4, 4, 4, 4, 4)

#Plotting board with heats, title, labels and a "legend"
ggplot(df) + 
  geom_tile(aes(x = x.pos, y = y.pos, width = w, height = h),
            size = 1, color = "black", fill = fills) +
  geom_text(aes(x = x.pos, y = y.pos, label = number), color = color, size = 6) +
  geom_text(aes(label = "
  0: Start
  10: Jail
  20: Free Parking
  30: Go To Jail", x = 12.5, y = 30), fontface = "italic", size = 6, hjust = 0) +
  geom_text(aes(label = "Monopoly Probability Heatmap", x = 0, y = 52),
            fontface = "bold", size = 7, hjust = 0) +
  geom_text(aes(label = "
Yellow -> HOT
Red -> COLD", x = 14, y = 18), size = 5, hjust = 0) +
  coord_fixed() +
  theme_void()
