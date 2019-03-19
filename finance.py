import sympy as sp

sp.init_printing()
x,eq_to_solve,output = sp.symbols('x,eq_to_solve,output')
ls = sp.Function('ls')
rs = sp.Function('rs')

#Future value simple intrest
def fv_si(pv, r, n):

   fv_si = pv*(1+n*r)

   return fv_si

#Present value simple intrest
def pv_si(fv, r, n):

   pv_si = fv/(1+n*r)

   return pv_si

#Future value compound intrest
def fv_ci(pv, r, n):

   fv_ci = pv*(pow(1+r,n))

   return fv_ci

#Present value compound intrest
def pv_ci(fv, r, n):

   pv_ci = fv/(pow(1+r,n))

   return pv_ci

def pv_p(c, r):

   pv_p = c/r

   return pv_p

def pv_dp(c,r,n):

   pv_dp = (c/r)*(1/pow(1+r,n))

   return pv_dp

def pv_oa(c,r,n):

   pv_oa = c/r * (1-1/pow(1+r,n))

   return pv_oa


#Future value of an ordinary annuity
def fv_oa(c,r,n):

   fv_oa = (c/r)*(pow((1+r),n) - 1)

   return fv_oa
   
def pv_ad(c,r,n):

   pv_ad = c/r * (1-1/pow(1+r,n))*(1+r)

   return pv_ad

def fv_ad(c,r,n):

   fv_ad = (c/r)*(pow(1+r,n)-1)*(1+r)

   return fv_ad

def pv_gp(c,r,g):

   pv_gp = c/(r-g)

   return pv_gp

def pv_goa(c, r, g, n):

   pv_goa = (c/(r-g))*(1-pow((1+g)/(1+r),n))

   return pv_goa

def fv_goa(c, r, g, n):

   fv_goa = (c/(r-g))*(1-pow((1+g)/(1+r),n))*pow(1+r,n)

   return fv_goa

def solver(ls, rs):
   
   eq_to_solve = sp.Eq(ls, rs)
   output = sp.solve(eq_to_solve,x)
   print("x = ", float(output[0]))

def main():
   
   help_needed = input("Do you need a list of functions available and their arguments, y/n? ")
   #help_needed = "n"
   if(help_needed == "y"):
      print("""Functions avaliable:
         fv_si(pv, r, n)
         pv_si(fv, r, n)
         fv_ci(pv, r, n)
         pv_ci(fv, r, n)
         pv_p(c, r)
         pv_dp(c,r,n)
         pv_oa(c,r,n)
         fv_oa(c,r,n)
         pv_ad(c,r,n)
         pv_gp(c,r,g)
         pv_goa(c, r, g, n)
         fv_goa(c, r, g, n)""")

   ls = eval(input("left side of equation? "))
   rs = eval(input("right side of equation? "))

   solver(ls,rs)

main()
