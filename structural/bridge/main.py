from bridge import *

def main():
    vector_renderer = VectorRenderer()
    raster_renderer = RasterRenderer()

    circle_vector = Circle(vector_renderer, 5)
    circle_rater = Circle(raster_renderer, 10)

    circle_vector.draw()
    circle_rater.draw()


    square_vector = Square(vector_renderer, 4, 6)
    square_raster = Square(raster_renderer, 8, 12)
    
    
    square_vector.draw()
    square_raster.draw()



if __name__ == "__main__":
    main()
