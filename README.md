# notion-extensions
Notion API Client and Extensions

## Todo

- [ ] Client Class
    - [ ] Pages
        - [x] Retrieve a page
        - [ ] Create a page
            - [x] create page in page
            - [x] create page in database
            - [ ] create page with children blocks
            - [ ] create page with icon
            - [ ] create page with cover
        - [ ] Update a page
            - [ ] update page with children blocks (name: properties)
            - [ ] archive (delete) or un-archive (restore)
            - [ ] update icon for page
            - [ ] update cover for page
        - [x] ~~Archive (delete) a page~~
        - [ ] Retrieve a page propoerty item
            - [ ] ...
    - [ ] Databeses
        - [ ] Query a database
        - [ ] Create a database
        - [ ] Update a database
        - [ ] Retrieve a database
        - [ ] ~~List databases (deprecated)~~
    - [ ] Blocks
        - [x] Retrieve a block
        - [ ] Update a block
            - [ ] archive (delete) or un-archive (restore)
            - [ ] update block type `text`
            - [ ] update block type `checked` (`to_do`)
        - [x] Retrieve block children
        - [ ] Append block children
        - [x] Delete a block
    - [ ] Users
        - [ ] Retrieve a user
        - [ ] List all users
        - [ ] Retrieve your token's bot user
    - [ ] Search
        - [ ] Search

- [ ] Property Values Object Classes??
     - [ ] page
     - [ ] database
     - [ ] block
     - [ ] user
     - [ ] common
        - [x] BaseProp
        - [x] Annotations
        - [x] PlainText
        - [x] Text
        - [x] RichText
        - [ ] Number
        - [ ] Select
        - [ ] MultiSelect
        - [ ] Date
        - [ ] Relation
        - [ ] Formula
        - [ ] Rollup
        - [ ] People
        - [ ] Files
        - [ ] Checkbox
        - [ ] Url
        - [ ] Email
        - [ ] PhoneNumber
        - [ ] CreatedTime
        - [ ] CreatedBy
        - [ ] LastEdited
        - [ ] LastEditedBy