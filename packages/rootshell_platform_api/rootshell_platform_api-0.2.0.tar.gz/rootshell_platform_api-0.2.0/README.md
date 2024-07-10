
A project to access Rootshell's Public API. 

`pip install rootshell_platform_api`

The `BEARER_TOKEN` can be accessed in the Platform. 
The `API_ENDPOINT` is the tenant url which you want access the data.
```shell
export BEARER_TOKEN=your_token_here
export API_ENDPOINT=https://your.api.endpoint
```

Currently list of groups that are accessible

```text

asset_groups_assets
    get-paginated
    update
    
asset_groups
    get-paginated
    get-single
    create
    update
    delete
 
asset_tags
    get-paginated
    update
    delete
    
assets 
    get-paginated
    get-single
    create
    update
    delete

companies
    get-paginated
    get_single

issue_comments
    get-paginated    
    create
    delete
    
 issues
    get-paginated
 
merge_settings
    get-paginated
    get-single
 
phase_host_issues
    get-paginated
    get-single
    create
    update
    delete

phase-hosts
    get-paginated
    get-single
    create
    update
    delete
 
phase_issues
    get-paginated
    get-single
    create
    update
    delete

phase_tags
    get-paginated
    delete
    update
     
phase_testers
    get-paginated
    update
    delete
    
phases 
    get-paginated
    get-single
    create
    update
    delete
    
projects
    get-paginated
    get-single
    create
    update
    delete
    
project_statuses
    get-paginated
    
project_remediation_types
    get-paginated
    
project_service_types
    get-paginated
    
project_statuses
    get-paginated
    
project-tags
    get-paginated
    update
    delete
    
tags
    get-paginated
    get-single
    create
    update
    delete
    
test_types
    get-paginated
    
users
    get-paginated
    

```
Example:
```shell
rootshell_platform tags get_paginated
```

