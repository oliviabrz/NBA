import { Component, OnInit, Input, OnChanges, SimpleChanges } from '@angular/core';
import { Team } from '../team';
import { TEAM } from '../mock-team';
import { Kvp } from '../kvp';
import { ApiDataService } from '../apiData/api.data.service';
import { MatTableDataSource } from '@angular/material/table';

@Component({
  selector: 'app-team',
  templateUrl: './team.component.html',
  styleUrls: ['./team.component.scss']
})
export class TeamComponent implements OnInit, OnChanges {
  @Input() selectedTeam?: Team;
  //team: Team = TEAM;
  //team: Team | undefined 
  dsTable: MatTableDataSource<Kvp>;
  tableData: Kvp[] | undefined;

  //selectedTeam?: Team;
  displayedColumns  :  string[] = ['Key', 'Value'] 
  
  constructor(private apiDataService: ApiDataService) { 
    this.dsTable = new MatTableDataSource<Kvp>();
  }

  ngOnInit(): void { }
    // this is mock data:
    //this.team = TEAM;

    // this is api data:
    //this.apiDataService.getTeam('ATL')
    //.subscribe((data) => {    
      //this.team = data;
      ngOnChanges(changes: SimpleChanges) {
        let team = changes['selectedTeam'].currentValue
      if (team != undefined) {
        console.info("in team-component ngOnChanges: selectedTeam not null");
      this.tableData = [
        {Key: 'Abbreviation', Value: team.Abbreviation},
        {Key: 'City', Value: team.City},
        {Key: 'Conference', Value: team.Conference},
        {Key: 'Division', Value: team.Division},
        {Key: 'FullName', Value: team.FullName},
        {Key: 'ID', Value: team.ID},
        {Key: 'Name', Value: team.Name},
      ];
      this.dsTable.data = this.tableData;
    }
    else {
      console.info("in player-component ngOnChanges: selectedTeam null");
    }   
  }
}

  // onSelect(team: Team): void {
  //   this.selectedTeam = team;
  // }

