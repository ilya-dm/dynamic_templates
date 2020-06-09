from django import template
register = template.Library()


@register.filter
def cell_color(cell):
    key = cell[0]
    value = cell[1]
    if key == "Год":
        return "white"
    elif key == "Суммарная":
        return "grey"
    else:
        try:
            if float(value) < 0:
                return "#90ee90"
            elif float(value) <= 1:
                return "white"
            elif float(value) <= 2:
                return "#FCD3D3"
            elif float(value) <= 5:
                return "#F98C8C"
            elif float(value) > 5:
                return "#FF0800"
        except ValueError:
            return 'white'
@register.filter
def cell_text(cell):
    if cell[1] != '':
        return cell[1]
    else:
        return '-'