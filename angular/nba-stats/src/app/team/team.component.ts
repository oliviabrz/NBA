import { Component, OnInit } from '@angular/core';
import { Team, Kvp } from '../team';
import { TEAM } from '../mock-team';
import { ApiDataService } from '../apiData/api.data.service';
import { MatTableDataSource } from '@angular/material/table';

@Component({
  selector: 'app-team',
  templateUrl: './team.component.html',
  styleUrls: ['./team.component.scss']
})
export class TeamComponent implements OnInit {

  team: Team = TEAM;
  dsTable: MatTableDataSource<Kvp>;
  tableData: Kvp[] | undefined;

  //selectedTeam?: Team;
  displayedColumns  :  string[] = ['Key', 'Value'] 
  
  constructor(private apiDataService: ApiDataService) { 
    this.dsTable = new MatTableDataSource<Kvp>();
  }

  ngOnInit(): void {
    this.tableData = [
      {Key: 'Abbreviation', Value: this.team.Abbreviation},
      {Key: 'City', Value: this.team.City},
      {Key: 'Conference', Value: this.team.Conference},
      {Key: 'Division', Value: this.team.Division},
      {Key: 'FullName', Value: this.team.FullName},
      {Key: 'ID', Value: this.team.ID},
      {Key: 'Name', Value: this.team.Name},
    ];
    this.dsTable.data = this.tableData;
    // let map = new Map();
    // map.set('Abbreviation', this.team.Abbreviation);
    // this.tableData.push(map)

    // map = new Map();
    // map.set('City', this.team.City);
    // this.tableData.push(map)

    // .subscribe((data) => {    
    //   this.teams = data
    // });
  }

  // onSelect(team: Team): void {
  //   this.selectedTeam = team;
  // }

}


