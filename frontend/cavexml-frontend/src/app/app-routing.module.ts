import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { AppComponent } from './app.component';
import { CavexmlSearchComponent } from './cavexml-search/cavexml-search.component';
import { MainPageComponent } from './main-page/main-page.component';


const routes: Routes = [
  {path:'', component: MainPageComponent},
  {path: 'cavexml', component: CavexmlSearchComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
