import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { MainProjectComponent } from './pages/main-project/main-project.component';

const routes: Routes = [
  {path: '', component:MainProjectComponent},
  {path: '**', redirectTo:""}
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class ProjectsRoutingModule { }
