head_labor = 45000 / 52
pt_labor_hour = 15
tr_sales = 30

consumables = {
    'ingredients_keg': int(15),
    'yeast_pitch': int(50),
    'chemicals_batch': int(5)
    }


def cost_per_keg(house_kegs_weekly):
    yeast_weekly = house_kegs_weekly / 6 * consumables['yeast_pitch']
    chemicals_weekly = house_kegs_weekly / 6 * consumables['chemicals_batch']
    if house_kegs_weekly > 18:
        pt_labor = ((house_kegs_weekly - 18) * ((house_kegs_weekly - 18) ** -.05) / 2) * pt_labor_hour
    else:
        pt_labor = 0
    total_labor = head_labor + pt_labor
    weekly_cost = house_kegs_weekly * consumables['ingredients_keg'] + yeast_weekly + chemicals_weekly + total_labor
    keg_cost = weekly_cost / house_kegs_weekly
    #print('Part-time labor cost per week for {} kegs: {}'.format(house_kegs_weekly, round(pt_labor,2)))
    return(keg_cost)


def keg_profit(house_kegs_weekly):
    if house_kegs_weekly < 30:
        guest_kegs = tr_sales - house_kegs_weekly
    else:
        guest_kegs = 0
    if house_kegs_weekly > 30:
        exp_profit = (house_kegs_weekly - 30) * (60 - cost_per_keg(house_kegs_weekly))
        house_profit = 30 * 202
        guest_profit = guest_kegs * 202
    else:
        guest_profit = guest_kegs * 202
        house_profit = house_kegs_weekly * (230 - 28)
        exp_profit = 0
    print('Export profit: {}'.format(exp_profit))
    total_profit = guest_profit + house_profit + exp_profit
    return total_profit



production_points = [10, 18, 24, 30, 36, 42, 48, 54, 60, 80, 100, 200]

for p in production_points:
    print('Cost per keg for {} kegs/week: {}'.format(p, round(cost_per_keg(p),2)))
    print()

for p in production_points:
    print('Potential profit at {} kegs/week: {}'.format(p, round(keg_profit(p),2)))
    print()