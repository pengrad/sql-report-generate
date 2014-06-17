sql-report-generate
===================

Generate sql-files by templates and variables

#### Example template (.tpl)
select * from game where GameId={game_id};

#### Example data
({"report_name": "iOS App", "game_id": 3},{"report_name": "Android App", "game_id": 4})
