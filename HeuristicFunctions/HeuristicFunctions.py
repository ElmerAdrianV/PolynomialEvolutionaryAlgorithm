import numpy as np
import numpy.polynomial as poly


class HeuristicFunctions:
    def __init__(self, heuristic_type):
        self.heuristic_type = heuristic_type
    def evaluate(self, polynomial):
        """
            Evaluates the polynomial using the heuristic function
        """
        if self.heuristic_type == "HVSymetry":
            return self.HorizontalVerticalSymetry(polynomial)
    
    def HorizontalVerticalSymetry(self, polynomial):
        ''' TODO 1: Check that the vertical values are not larger than the x-values
                and give lower fitness if they are
        '''
        # Find the "ideal" x-values for the local minima/maxima of the
        # polynomial (relative to the minimum and maximum x-values
        # included in the graph, which are set based on the smallest
        # and largest real x-values for the minima/maxima):
        ideal=[polynomial.x_values[0]+(polynomial.x_values[-1]-polynomial.x_values[0])*0.25,
               polynomial.x_values[0]+(polynomial.x_values[-1]-polynomial.x_values[0])*0.5,
               polynomial.x_values[0]+(polynomial.x_values[-1]-polynomial.x_values[0])*0.75]
        
        # Find the width of the interval between adjacent ideal x-values:
        interval_width=(polynomial.x_values[-1]-polynomial.x_values[0])*0.25
        
        # Find the equation of the derivative of the polynomial:
        deriv=poly.polynomial.polyder(polynomial.coefficients)
        
        # Find the roots of the derivative, thus finding the x-values at
        # which the original polynomial reaches a local minimum or
        # maximum:
        roots=poly.polynomial.polyroots(deriv)

        # Measure the "quality" of each actual x-value (of the minima
        # and maxima) by finding how far it is from the ideal value as a
        # fraction of the interval width:
        x_qualities=[]
        for i in range(0,len(roots)):
            if ideal[i]>roots[i]:
                deviation=ideal[i]-roots[i]
            else:
                deviation=roots[i]-ideal[i]
            #deviation=abs(ideal[i]-roots[i])
            # Occasionally there will be a deviation of more than one
            # interval width between some real x-value and its
            # corresponding ideal x-value, and this extreme situation
            # is dealt with by forcing the quality of the corresponding
            # x-value to be equal to 0 automatically, rather than
            # relying on the more general quality measurement algorithm
            # above:
            if deviation>interval_width:
                deviation=interval_width
            x_qualities.append((interval_width-deviation)/interval_width)
        
        # Calculate the "global" x-value quality by finding the mean of
        # the qualities of each individual x-value:
        x_quality=sum(x_qualities)/len(x_qualities)
        
        # Find the y-values of the original polynomial at the x-values
        # corresponding to the local minima/maxima:
        y_roots=[]
        for r in roots:
            y_roots.append(polynomial.polynomial_function_evaluate(r))
        # Find the y-values of the original polynomial at the extreme
        # x-values of the part of the polynomial being considered, and
        # then find the minimum and maximum y-values present in that
        # part of the polynomial, in order to find the height of the
        # part of the polynomial being considered:
        y_val_left=polynomial.polynomial_function_evaluate(polynomial.x_values[0])
        y_val_right=polynomial.polynomial_function_evaluate(polynomial.x_values[-1])
        max_y=max(y_val_left,y_val_right)
        min_y=min(y_roots)
        interval_height=max_y-min_y

        # Measure the global "quality" of the y-values by measuring
        # how far the y-value of the minima are from each other as a
        # fraction of the interval height.  NOTE 1: this calculation
        # only makes sense for degree-4 polynomials (which will have
        # two minima and one maximum).  NOTE 2: the y-value of the
        # maximum is currently ignored:
        y_quality=(interval_height-abs(y_roots[0]-y_roots[2]))/interval_height
        
        # Find the mean of the x-quality and y-quality values to find
        # the global fitness value:
        global_quality=(x_quality+y_quality)/2
            
        return global_quality, x_quality,y_quality
        