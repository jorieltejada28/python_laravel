<?php

namespace Database\Seeders;

use App\Models\Employee;
use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;

class EmployeeSeeder extends Seeder
{
    /**
     * Run the database seeds.
     */
    public function run(): void
    {
         // Insert sample employees
         Employee::insert([
            // Software Engineers
            [
                'name' => 'John Doe',
                'email' => 'john@example.com',
                'position' => 'Software Engineer',
                'salary' => 60000.00,
                'created_at' => now(),
                'updated_at' => now(),
            ],
            [
                'name' => 'Emma Brown',
                'email' => 'emma@example.com',
                'position' => 'Software Engineer',
                'salary' => 65000.00,
                'created_at' => now(),
                'updated_at' => now(),
            ],
            [
                'name' => 'David Wilson',
                'email' => 'david@example.com',
                'position' => 'Software Engineer',
                'salary' => 70000.00,
                'created_at' => now(),
                'updated_at' => now(),
            ],
            [
                'name' => 'Lucas Turner',
                'email' => 'lucas@example.com',
                'position' => 'Software Engineer',
                'salary' => 72000.00,
                'created_at' => now(),
                'updated_at' => now(),
            ],
            [
                'name' => 'Sophia Evans',
                'email' => 'sophia.evans@example.com',
                'position' => 'Software Engineer',
                'salary' => 68000.00,
                'created_at' => now(),
                'updated_at' => now(),
            ],

            // Project Managers
            [
                'name' => 'Jane Smith',
                'email' => 'jane@example.com',
                'position' => 'Project Manager',
                'salary' => 80000.00,
                'created_at' => now(),
                'updated_at' => now(),
            ],
            [
                'name' => 'Michael Johnson',
                'email' => 'michael@example.com',
                'position' => 'Project Manager',
                'salary' => 85000.00,
                'created_at' => now(),
                'updated_at' => now(),
            ],
            [
                'name' => 'Sophia Martinez',
                'email' => 'sophia@example.com',
                'position' => 'Project Manager',
                'salary' => 90000.00,
                'created_at' => now(),
                'updated_at' => now(),
            ],
            [
                'name' => 'Liam Scott',
                'email' => 'liam.scott@example.com',
                'position' => 'Project Manager',
                'salary' => 88000.00,
                'created_at' => now(),
                'updated_at' => now(),
            ],

            // Data Analysts
            [
                'name' => 'Alice Johnson',
                'email' => 'alice@example.com',
                'position' => 'Data Analyst',
                'salary' => 55000.00,
                'created_at' => now(),
                'updated_at' => now(),
            ],
            [
                'name' => 'Liam Anderson',
                'email' => 'liam@example.com',
                'position' => 'Data Analyst',
                'salary' => 58000.00,
                'created_at' => now(),
                'updated_at' => now(),
            ],
            [
                'name' => 'Olivia Thomas',
                'email' => 'olivia@example.com',
                'position' => 'Data Analyst',
                'salary' => 60000.00,
                'created_at' => now(),
                'updated_at' => now(),
            ],
            [
                'name' => 'Noah White',
                'email' => 'noah.white@example.com',
                'position' => 'Data Analyst',
                'salary' => 62000.00,
                'created_at' => now(),
                'updated_at' => now(),
            ],

            // UI/UX Designers
            [
                'name' => 'Ella Moore',
                'email' => 'ella@example.com',
                'position' => 'UI/UX Designer',
                'salary' => 64000.00,
                'created_at' => now(),
                'updated_at' => now(),
            ],
            [
                'name' => 'James Hall',
                'email' => 'james@example.com',
                'position' => 'UI/UX Designer',
                'salary' => 66000.00,
                'created_at' => now(),
                'updated_at' => now(),
            ],
            [
                'name' => 'Charlotte Lewis',
                'email' => 'charlotte@example.com',
                'position' => 'UI/UX Designer',
                'salary' => 68000.00,
                'created_at' => now(),
                'updated_at' => now(),
            ],

            // HR Specialists
            [
                'name' => 'Ethan Walker',
                'email' => 'ethan@example.com',
                'position' => 'HR Specialist',
                'salary' => 60000.00,
                'created_at' => now(),
                'updated_at' => now(),
            ],
            [
                'name' => 'Amelia Adams',
                'email' => 'amelia@example.com',
                'position' => 'HR Specialist',
                'salary' => 62000.00,
                'created_at' => now(),
                'updated_at' => now(),
            ]
        ]);
    }
}
