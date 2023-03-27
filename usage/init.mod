
variable up equal 1.0e-6
variable atomjiggle equal 1.0e-5

units           metal
variable cfac equal 1.0e-4
variable cunits string GPa

# Define minimization parameters
variable etol equal 1.0e-15
variable ftol equal 1.0e-10
variable maxiter equal 400000
variable maxeval equal 400000
variable dmax equal 1.0e-2

atom_style atomic
boundary p p p
box tilt large

read_data       data.relax
