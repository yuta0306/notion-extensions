# notion-extensions
Notion API Client and Extensions

## Todo

- [ ] Client Class
    - [ ] Pages
        - [x] Retrieve a page
        - [x] Create a page
            - [x] create page in page
            - [x] create page in database
            - [x] create page with children blocks
            - [x] create page with icon
            - [x] create page with cover
        - [x] Update a page
            - [x] update page (name: properties (Title only))
            - [x] archive (delete) or un-archive (restore)
            - [x] update icon for page
            - [x] update cover for page
        - [x] ~~Archive (delete) a page~~
        - [ ] Retrieve a page propoerty item
            - [ ] ...
    - [ ] Databeses
        - [ ] Query a database
        - [ ] Create a database
        - [ ] Update a database
        - [x] Retrieve a database
        - [ ] ~~List databases (deprecated)~~
    - [ ] Blocks
        - [x] Retrieve a block
        - [ ] Update a block
            - [ ] archive (delete) or un-archive (restore)
            - [ ] update block type `text`
            - [ ] update block type `checked` (`to_do`)
        - [x] Retrieve block children
        - [x] Append block children
        - [x] Delete a block
    - [ ] Users
        - [ ] Retrieve a user
        - [ ] List all users
        - [ ] Retrieve your token's bot user
    - [ ] Search
        - [ ] Search

- [ ] Property Values Object Classes??
     - [ ] page
        - [x] Title
     - [ ] database
        - [ ] Title
        - [x] Option
        - [x] Select
        - [x] MultiSelect
        - [x] Number
     - [x] block
        - [x] Block
        - [x] Children
        - [x] Paragraph
        - [x] Heading1
        - [x] Heading2
        - [x] Heading3
        - [x] Callout
        - [x] Quote
        - [x] BulletedListItem
        - [x] BulletedList
        - [x] NumberedListItem
        - [x] NumberedList
        - [x] ToDo
        - [x] ToDoList
        - [x] Toggle
        - [x] Code
        - [ ] ~~ChildPage~~
        - [ ] ~~ChildDatabase~~
        - [x] Embed
        - [x] Image
        - [x] Video
        - [x] File
        - [x] Pdf
        - [x] Bookmark
        - [x] Equation
        - [x] Divider
        - [x] TableOfContents
        - [x] BreadCrumb
        - [x] ColumnList
        - [x] Column
        - [ ] ~~LinkPreview~~
            - This cannot be used via API
        - [ ] ~~Template~~
        - [x] LinkToPage
        - [ ] ~~Synced~~
        - [x] OriginalSynced
        - [x] ReferenceSynced
        - [ ] ~~SyncedFrom~~
        - [x] Table
        - [x] TableRow
     - [ ] user
     - [ ] common
        - [x] BaseProp
        - [x] Annotations
        - [x] PlainText
        - [ ] Text
            - [x] text
            - [ ] mention
            - [ ] equation 
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
        - [x] FileObject
        - [x] Emoji
        - [x] Icon
        - [x] Cover