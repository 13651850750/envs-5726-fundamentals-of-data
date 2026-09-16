def is_min_ratio_toilets_to_people_met(ratio):
    ratio_parts = ratio.replace("t", "").replace("p", "").split("/")

    toilets = int(ratio_parts[0])
    people = int(ratio_parts[1])

    return toilets / people >= 1 / 20


print(is_min_ratio_toilets_to_people_met("1t/37p"))
print(is_min_ratio_toilets_to_people_met("1t/12p"))


def is_population_disabled(disabled, total_population):
    return disabled / total_population >= 0.10


print(is_population_disabled(disabled=0, total_population=32))
print(is_population_disabled(disabled=52, total_population=392))



def is_gp_religious_or_academic(gp):
    gp_words = set(gp.split())

    religious_words = {"Mosque", "Church"}
    academic_words = {"School", "Institute", "Education", "Faculty"}

    all_target_words = religious_words.union(academic_words)

    return bool(gp_words.intersection(all_target_words))


print(is_gp_religious_or_academic(
    "Faculty Of Earth Sciences and Mining"
))

print(is_gp_religious_or_academic(
    "Almorada Church"
))

print(is_gp_religious_or_academic(
    "Health Insulation Building"
))



def get_sanitation_priority(ratio, disabled, pop, gp):
    ratio_met = is_min_ratio_toilets_to_people_met(ratio)
    population_disabled = is_population_disabled(disabled, pop)
    religious_or_academic = is_gp_religious_or_academic(gp)

    if not ratio_met and population_disabled and religious_or_academic:
        return "High Priority"

    elif ratio_met and not population_disabled and not religious_or_academic:
        return "Low Priority"

    else:
        return "Medium Priority"


print(get_sanitation_priority(
    ratio="1t/49p",
    disabled=52,
    pop=392,
    gp="Faculty - Students Dwelling"
))

print(get_sanitation_priority(
    ratio="1t/29p",
    disabled=0,
    pop=178,
    gp="Mohamed Ali Abbas Secondary School For Girls"
))

print(get_sanitation_priority(
    ratio="1t/17p",
    disabled=0,
    pop=52,
    gp="Alsalam Old Mosque"
))

print(get_sanitation_priority(
    ratio="1t/6p",
    disabled=0,
    pop=12,
    gp="Nile Club"
))