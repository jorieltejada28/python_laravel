<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Http;
use Exception;

class ScheduleController extends Controller
{
    public function scheduleList()
    {
        try {
            $response = Http::timeout(5)->get('http://localhost:5000/generate-schedule');

            if ($response->successful()) {
                $schedule = $response->json();
                return view('schedule', ['schedule' => $schedule, 'error' => null]);
            } else {
                throw new Exception("Flask API responded with an error.");
            }
        } catch (Exception $e) {
            return view('schedule', ['schedule' => [], 'error' => 'Flask API is not running. Please start the server.']);
        }
    }
}
