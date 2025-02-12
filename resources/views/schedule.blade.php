@extends('layouts.main')

@section('title', 'Schedule')

@section('content')
    <div class="container mt-4">
        <div class="d-flex justify-content-between align-items-center mb-4">
            <h2>Weekly Schedule</h2>
            <a href="{{ route('home') }}" class="btn btn-primary">Back</a>
        </div>

        @if (!empty($error))
            <div class="alert alert-danger text-center">
                <strong>Error:</strong> {{ $error }}
            </div>
        @elseif (!empty($schedule) && !isset($schedule['error']))
            <div class="table-responsive">
                <table class="table table-bordered table-hover text-center">
                    <thead class="table-dark">
                        <tr>
                            <th>Day</th>
                            <th>08:00 AM - 04:00 PM</th>
                            <th>04:00 PM - 12:00 AM</th>
                        </tr>
                    </thead>
                    <tbody>
                        @foreach ($schedule as $row)
                            <tr>
                                <td>{{ $row['Day'] }}</td>
                                @foreach ([
                                    '08:00 AM - 04:00 PM',
                                    '04:00 PM - 12:00 AM'] as $slot)
                                    <td style="white-space: pre-line;">{{ str_replace(',', "\n", $row[$slot] ?? '') }}</td>
                                @endforeach
                            </tr>
                        @endforeach
                    </tbody>
                </table>
            </div>
        @else
            <div class="alert alert-warning text-center">
                <strong>Notice:</strong> No employees found in the database. Please add employees to generate a schedule.
            </div>
        @endif
    </div>
@endsection
