@extends('layouts.main')

@section('title', Employees Registration)

@section('content')
    <div class="container mt-4">
        <div class="d-flex justify-content-between align-items-center mb-4">
            <h2>Registration of Employees</h2>
            <a href="{{ route('home') }}" class="btn btn-primary">Back</a>
        </div>

    </div>
@endsection
