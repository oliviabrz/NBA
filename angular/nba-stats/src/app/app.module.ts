import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms'; // <-- NgModel lives here
import { MatTableModule } from "@angular/material/table";
import { MatPaginatorModule } from '@angular/material/paginator';
import { MatSelectModule } from '@angular/material/select';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MatButtonModule } from '@angular/material/button';
import { MatToolbarModule } from '@angular/material/toolbar';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { KeyValuePipeComponent } from './keyvalue-pipe/keyvalue-pipe.component';
import { NgxEchartsModule } from 'ngx-echarts';
//import { ChartsModule } from 'ng2-charts';
import { MatInputModule } from '@angular/material/input';

import { PlayersComponent } from './players/players.component';
import { TeamComponent } from './team/team.component';
import { PlayerComponent } from './player/player.component';
import { TeamListComponent } from './team-list/team-list.component';
import { GameListComponent } from './game-list/game-list.component';
import { MenuComponent } from './menu/menu.component';
import { GameStatsComponent } from './game-stats/game-stats.component';
import { DatePipe } from '@angular/common';

@NgModule({
  declarations: [
    AppComponent,
    PlayersComponent,
    TeamComponent,
    KeyValuePipeComponent,
    PlayerComponent,
    TeamListComponent,
    GameListComponent,
    MenuComponent,
    GameStatsComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    AppRoutingModule,
    FormsModule,
    MatTableModule,
    MatPaginatorModule,
    MatSelectModule,
    BrowserAnimationsModule,
    MatButtonModule,
    MatToolbarModule,
    NgxEchartsModule.forRoot({
      echarts: () => import('echarts'),
    }),
    //ChartsModule
    MatInputModule,
  ],
  providers: [DatePipe],
  bootstrap: [AppComponent]
})
export class AppModule { }
