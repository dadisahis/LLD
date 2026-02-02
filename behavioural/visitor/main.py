from visitor import *


def main():
    shapes = [
        Circle(5),
        Square(4),
        Circle(3),
    ]

    print("Calculating Areas:")
    for s in shapes:
        area_calculator=  AreaCalculator()
        s.accept(area_calculator)
    
    print("SVG Export:")
    for s in shapes:
        svg_exporter = SVGEXporter()
        s.accept(svg_exporter)

if __name__ == "__main__":
    main()