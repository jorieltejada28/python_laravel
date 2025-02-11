<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\ScheduleController;
use App\Http\Controllers\EmployeeController;

Route::get('/', [EmployeeController::class, 'index'])->name('home');
Route::get('/schedule', [ScheduleController::class, 'scheduleList'])->name('schedule');
