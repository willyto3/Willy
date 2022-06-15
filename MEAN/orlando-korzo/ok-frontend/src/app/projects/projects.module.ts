import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { ProjectsRoutingModule } from './projects-routing.module';
import { MainProjectComponent } from './pages/main-project/main-project.component';

@NgModule({
  declarations: [MainProjectComponent],
  imports: [CommonModule, ProjectsRoutingModule],
})
export class ProjectsModule {}
