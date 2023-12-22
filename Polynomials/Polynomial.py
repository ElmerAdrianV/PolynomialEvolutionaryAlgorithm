# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 09:30:25 2023

@author: andre
"""

import random
import numpy as np
import numpy.polynomial as poly
import matplotlib.pyplot as plt


# Represents polynomials of degree 4 whose roots will be initialized
# randomly (the roots will be real numbers):
class poly4:
    def __init__(self, roots, deg=4, comments = False):
        self.deg= deg
        if comments:
            print("Degree:",self.deg)
        self.roots= roots  # The roots will be stored in a list
        # Finds the coefficients of the polynomial by multiplying the
        # linear factors of the polynomial (based on the root values).
        # If the degree in 0 then there won't have been any roots found
        # earlier and the coefficient of the constant (only) term of
        # the polynomial will be set randomly:
        if np.iscomplex(self.roots).any():
            self.global_fitness,self.horiz_fitness,self.vert_fitness=0,0,0
        else: 
            self.coefficients=[]
            if self.deg==0:
                self.coefficients.append(random.uniform(-10,10))
            else:
                # The polynomial in factorized form is constructed based on
                # the roots:
                poly_factorized=[]
                for i in range(0,len(self.roots)):
                    poly_factorized.append([-self.roots[i],1])
                if comments:
                    print("Factorized polynomial:",poly_factorized)
                self.coefficients=poly_factorized[0]
                for i in range(1,len(poly_factorized)):
                    self.coefficients=self.multiply(self.coefficients,poly_factorized[i])
            if comments:
                print("Coefficients:",self.coefficients)
            x_values,y_values=self.graph_polyn()
            self.global_fitness,self.horiz_fitness,self.vert_fitness=self.evaluate_poly(x_values,y_values)

    # Creates a list containing the specified number of 0's in it:
    def list_of_zeros(self,num):
        res=[]
        for i in range(0,num-1):
            res.append(0)
        return res

    # Multiplies two polynomials (each provided as a separate argument
    # specified as a list of coefficients from the lowest-order one to
    # the highest-order one):
    def multiply(self,poly1,poly2):
        #print("Polynomials to multiply:",poly1,poly2)
        # The degree of the resulting polynomial will be the sum of the
        # degrees of the original polynomials:
        deg_res=len(poly1)+len(poly2)-1
        # Create a list with "deg_res" 0's in it:
        res=self.list_of_zeros(deg_res+1)
        #print(res)
        for i in range(0,len(poly1)):
            for j in range(0,len(poly2)):
                #print(i,j,i+j)
                res[i+j]=res[i+j]+poly1[i]*poly2[j]
        #print("Result of multiplication:",res)
        return res
    
    # Returns the result of evaluating the polynomial at the value
    # specified in the argument:
    def polyn(self,val):
        res=0
        for i in range(0,len(self.coefficients)):
            #print(i)
            res=res+self.coefficients[i]*val**i
        return res
            
    # Graphs the polynomial function:    
    def graph_polyn(self, plot=False, comments = False):
        # If the polynomial degree is smaller than or equal to 1, the
        # limits will automatically be set to (-15,15), or to a
        # displacement by these amounts from the root, respectively:
        if len(self.roots)==0:
            low_lim=-15
            upp_lim=15
        elif len(self.roots)==1:
            low_lim=self.roots[0]-15
            upp_lim=self.roots[0]+15
        # Otherwise the limits will be set according to the smallest and
        # highest roots (plus/minus a displacement of 10% of the
        # difference):
        else:
            smallest=min(self.roots)
            largest=max(self.roots)
            if largest - smallest > 10**-5: 
                diff=largest-smallest
            else:
                diff = largest
            low_lim=smallest-diff*0.1
            upp_lim=largest+diff*0.1
        if comments:
            print("Smallest- and highest-value roots:",low_lim,upp_lim)
        # Creates a list of 50 evenly-spaced x-values between the two
        # specified limits:
        x_values=np.linspace(low_lim,upp_lim)
        y_values=[]
        for x in x_values:
            y_values.append(self.polyn(x))
        if plot:
            print("X-points:",x_values)
            print("Y-points:",y_values)
            plt.plot(x_values,y_values)
            plt.show()
        return x_values,y_values
    
    # Evaluates the aesthetics of the graph of the polynomial function:
    def evaluate_poly(self,x_values,y_values, comments = False):
        ''' TODO 1: Check that the vertical values are not larger than the x-values
                and give lower fitness if they are
        '''

        # Find the "ideal" x-values for the local minima/maxima of the
        # polynomial (relative to the minimum and maximum x-values
        # included in the graph, which are set based on the smallest
        # and largest real x-values for the minima/maxima):
        ideal=[x_values[0]+(x_values[-1]-x_values[0])*0.25,
               x_values[0]+(x_values[-1]-x_values[0])*0.5,
               x_values[0]+(x_values[-1]-x_values[0])*0.75]
        if comments:
            print("Ideal x-values for minima and maxima:",ideal)
        # Find the width of the interval between adjacent ideal x-values:
        interval_width=(x_values[-1]-x_values[0])*0.25
        if comments:
            print("Interval width:",interval_width)
        # Find the equation of the derivative of the polynomial:
        deriv=poly.polynomial.polyder(self.coefficients)
        if comments:
            print("Derivative polynomial:",deriv)
        # Find the roots of the derivative, thus finding the x-values at
        # which the original polynomial reaches a local minimum or
        # maximum:
        roots=poly.polynomial.polyroots(deriv)
        if comments:
            print("Actual x-values for minima and maxima:",roots)
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
            if comments:
                print("Deviation:",deviation)
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
        if comments:
            print("Quality of real x-values:",x_qualities)
        # Calculate the "global" x-value quality by finding the mean of
        # the qualities of each individual x-value:
        x_quality=sum(x_qualities)/len(x_qualities)
        if comments:
            print("x-quality:",x_quality)
        
        # Find the y-values of the original polynomial at the x-values
        # corresponding to the local minima/maxima:
        y_roots=[]
        for r in roots:
            y_roots.append(self.polyn(r))
        # Find the y-values of the original polynomial at the extreme
        # x-values of the part of the polynomial being considered, and
        # then find the minimum and maximum y-values present in that
        # part of the polynomial, in order to find the height of the
        # part of the polynomial being considered:
        y_val_left=self.polyn(x_values[0])
        y_val_right=self.polyn(x_values[-1])
        max_y=max(y_val_left,y_val_right)
        min_y=min(y_roots)
        interval_height=max_y-min_y
        if comments:
            print("Interval height:",interval_height)
        # Measure the global "quality" of the y-values by measuring
        # how far the y-value of the minima are from each other as a
        # fraction of the interval height.  NOTE 1: this calculation
        # only makes sense for degree-4 polynomials (which will have
        # two minima and one maximum).  NOTE 2: the y-value of the
        # maximum is currently ignored:
        y_quality=(interval_height-abs(y_roots[0]-y_roots[2]))/interval_height
        if comments:
            print("y-value left minimum, y-value right minimum, difference:",y_roots[0],y_roots[2],abs(y_roots[0]-y_roots[2]))
        if comments:
            print("y-quality:",y_quality)
        
        # Find the mean of the x-quality and y-quality values to find
        # the global fitness value:
        global_quality=(x_quality+y_quality)/2
        if comments:
            print("Global quality:",global_quality)
            
        return global_quality, x_quality,y_quality





