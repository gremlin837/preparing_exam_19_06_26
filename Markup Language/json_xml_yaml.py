# Один и тот же объект в трёх форматах:

# JSON
json_repr = """
{
  "user": {
    "id": 1,
    "name": "Анна",
    "active": true,
    "score": 98.5,
    "tags": ["admin", "editor"],
    "address": null
  }
}
"""

# YAML
yaml_repr = """
# Профиль пользователя
user:
  id: 1
  name: Анна
  active: true
  score: 98.5
  tags:
    - admin
    - editor
  address: ~
"""

# XML
xml_repr = """
<?xml version="1.0" encoding="UTF-8"?>
<user id="1" active="true">
  <name>Анна</name>
  <score>98.5</score>
  <tags>
    <tag>admin</tag>
    <tag>editor</tag>
  </tags>
  <address/>
</user>
"""

# Размер каждого представления:
print(f"JSON: {len(json_repr):>4} символов")   # ~120
print(f"YAML: {len(yaml_repr):>4} символов")   # ~100
print(f"XML:  {len(xml_repr):>4} символов")    # ~200