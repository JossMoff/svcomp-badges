# svcomp-badges
A convenience tool to proudly display your verfier/validators results from SVCOMP categories. It is a publically deployed API available at [svcompbadges.api.joss.dev](svcompbadges.api.joss.dev)
## Routes
See the [swagger file](https://github.com/JossMoff/svcomp-badges/blob/main/swagger.json) for the API definition.
## Examples
![Overall Winner Badge '23](https://img.shields.io/endpoint?style=flat-square&url=https%3A%2F%2Fsvcompbadges.api.joss.dev%2Fbadge%2F2023%3Fposition%3D1%26category%3D%2522Overall%2522)

Request: `svcompbadges.api.joss.dev/2023?position=1&category="Overall"`
```markdown
![Overall Winner Badge '23](https://img.shields.io/endpoint?style=flat-square&url=https%3A%2F%2Fsvcompbadges.api.joss.dev%2Fbadge%2F2023%3Fposition%3D1%26category%3D%2522Overall%2522))
```

![ReachSafety Second Badge '23](https://img.shields.io/endpoint?url=https%3A%2F%2Fsvcompbadges.api.joss.dev%2Fbadge%2F2022%3Fposition%3D2%26category%3D%2522ReachSafety%2522)

Request: `svcompbadges.api.joss.dev/2022?position=2&category="ReachSafety"`
```markdown
![ReachSafety Second Badge '23](https://img.shields.io/endpoint?url=https%3A%2F%2Fsvcompbadges.api.joss.dev%2Fbadge%2F2022%3Fposition%3D2%26category%3D%2522ReachSafety%2522)

```
![JavaOverall Third Badge '23](https://img.shields.io/endpoint?style=plastic&url=https%3A%2F%2Fsvcompbadges.api.joss.dev%2Fbadge%2F2023%3Fposition%3D3%26category%3D%2522JavaOverall%2522)

Request: `svcompbadges.api.joss.dev/2023?position=3&category="JavaOverall"`
```markdown
![JavaOverall Third Badge '23](https://img.shields.io/endpoint?url=https%3A%2F%2Fsvcompbadges.api.joss.dev%2Fbadge%2F2023%3Fposition%3D3%26category%3D%2522JavaOverall%2522)
```