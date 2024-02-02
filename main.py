def solve_cylinder_volume(radius_value, height_value):
    radius_sqared = radius_value * radius_value * 3.14
    sec_fn = radius_sqared * height_value

    return sec_fn
def solve_cone_volume(radius_value, height_value):
    radius_sqared = radius_value * radius_value * 3.14
    sec_fn = radius_sqared * height_value
    fn_vl = sec_fn / 3
    return fn_vl

calc_md = input(("Would you like the volume of a cone or cylinder calculated: "))
if calc_md == "cone":
    users_radius = int(input("Enter the radius of the cone: "))
    users_height = int(input("Enter the height of the cone: "))
    cone_volume = solve_cone_volume(users_radius, users_height)
    print(f"The volume of the cone is: {cone_volume}")
elif calc_md == "cylinder":
    users_radius = int(input("Enter radius of the cylinder: "))
    users_height = int(input("Enter the height of the cylinder: "))
    cylinder_volume = solve_cylinder_volume(users_radius, users_height)
    print(f"The volume of the cylinder is: {cylinder_volume}")
