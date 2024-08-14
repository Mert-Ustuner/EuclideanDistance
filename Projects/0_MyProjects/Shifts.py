import random

groups = {
    'A': ['Ali', 'Ayşe'],
    'B': ['Mehmet', 'Zeynep'],
    'C': ['Fatma', 'Hasan'],
    'D': ['Elif', 'Kemal']
}

shifts = {
    'A': '00:00-08:00',
    'B': '08:00-16:00',
    'C': '16:00-00:00'
}

shift_hours = {'00:00-08:00': 8, '08:00-16:00': 8, '16:00-00:00': 8}

employee_hours = {emp: 0 for group in groups.values() for emp in group}

schedule = {
    'Pazartesi': {'00:00-08:00': [], '08:00-16:00': [], '16:00-00:00': []},
    'Salı': {'00:00-08:00': [], '08:00-16:00': [], '16:00-00:00': []},
    'Çarşamba': {'00:00-08:00': [], '08:00-16:00': [], '16:00-00:00': []},
    'Perşembe': {'00:00-08:00': [], '08:00-16:00': [], '16:00-00:00': []},
    'Cuma': {'00:00-08:00': [], '08:00-16:00': [], '16:00-00:00': []},
    'Cumartesi': {'00:00-08:00': [], '08:00-16:00': [], '16:00-00:00': []},
    'Pazar': {'00:00-08:00': [], '08:00-16:00': [], '16:00-00:00': []}
}


def assign_shifts(groups, schedule, shifts, employee_hours, shift_hours):
    days = list(schedule.keys())
    for day in days:
        available_groups = list(groups.keys())
        for shift in shift_hours.keys():
            # Mevcut grupta kalamayacak bir çalışan varsa, en az saatle çalışanı bul
            group = random.choice(available_groups)
            available_groups.remove(group)
            assigned = False

            for employee in groups[group]:
                if employee_hours[employee] < max(employee_hours.values()):
                    schedule[day][shift].append(employee)
                    employee_hours[employee] += shift_hours[shift]
                    assigned = True
                    break

            # Eğer tüm çalışanlar doluysa, en az saatle çalışanı seç
            if not assigned:
                least_hours_employee = min(groups[group], key=lambda emp: employee_hours[emp])
                schedule[day][shift].append(least_hours_employee)
                employee_hours[least_hours_employee] += shift_hours[shift]

            # Üst üste 3 vardiya çalışmayı engellemek için bir sonraki gün aynı grubu çıkartalım
            if day != days[-1]:  # Son gün değilse
                next_day = days[days.index(day) + 1]
                next_shifts = list(schedule[next_day].values())
                if len(next_shifts) >= 2:
                    next_shifts[-2:] = [g for g in next_shifts[-2:] if g != groups[group]]

    return schedule


schedule = assign_shifts(groups, schedule, shifts, employee_hours, shift_hours)

for day, shifts in schedule.items():
    print(f"{day}: {shifts}")

print("\nÇalışanların toplam vardiya saatleri:")
for emp, hours in employee_hours.items():
    print(f"{emp}: {hours} saat")
